#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is part of web2py Web Framework (Copyrighted, 2007-2014).
Developed by Massimo Di Pierro <mdipierro@cs.depaul.edu>.
License: LGPL v3

Login will be done via Web2py's CAS application, instead of web2py's
login form.

Include in your model (eg db.py)::

    auth.define_tables(username=True)
    from gluon.contrib.login_methods.saml2_auth import Saml2Auth
    import os
    auth.settings.login_form=Saml2Auth(
    config_file = os.path.join(request.folder,'private','sp_conf'),
    maps=dict(
        username=lambda v: v['http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn'][0],
        email=lambda v: v['http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn'][0],
        user_id=lambda v: v['http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn'][0]))
        
you must have private/sp_conf.py, the pysaml2 sp configuration file. For example:


    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
    import os.path
    import requests
    import tempfile

    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    # Web2py SP url and application name
    HOST = 'http://127.0.0.1:8000'
    APP = 'sp'

    # To load the IDP metadata...
    IDP_METADATA = 'http://127.0.0.1:8088/metadata'

    def full_path(local_file):
        return os.path.join(BASEDIR, local_file)

    CONFIG = {                
        # your entity id, usually your subdomain plus the url to the metadata view.
        'entityid': '%s/%s/default/metadata' % (HOST, APP),
        'service': {
            'sp' : {
                'name': 'MYSP',  
                'endpoints': {     
                    'assertion_consumer_service': [
                        ('%s/%s/default/user/login' % (HOST, APP), BINDING_HTTP_REDIRECT),
                        ('%s/%s/default/user/login' % (HOST, APP), BINDING_HTTP_POST),       
                        ],
                    },
                },
            },
        # Your private and public key.
        'key_file': full_path('pki/mykey.pem'),
        'cert_file': full_path('pki/mycert.pem'),
        
        # where the remote metadata is stored
        'metadata': {
            "remote": [{
                "url": IDP_METADATA,
                "cert":full_path('pki/mycert.pem')
                }]
            },
    }

"""

import os
import types

from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
from saml2.client import Saml2Client

from gluon import URL, current, redirect
from gluon.utils import web2py_uuid


def obj2dict(obj, processed=None):
    """
    converts any object into a dict, recursively
    """
    processed = processed if not processed is None else set()
    if obj is None:
        return None
    if isinstance(obj, (int, long, str, unicode, float, bool)):
        return obj
    if id(obj) in processed:
        return "<reference>"
    processed.add(id(obj))
    if isinstance(obj, (list, tuple)):
        return [obj2dict(item, processed) for item in obj]
    if not isinstance(obj, dict) and hasattr(obj, "__dict__"):
        obj = obj.__dict__
    else:
        return repr(obj)
    return dict(
        (key, obj2dict(value, processed))
        for key, value in obj.items()
        if not key.startswith("_")
        and not type(value)
        in (
            types.FunctionType,
            types.LambdaType,
            types.BuiltinFunctionType,
            types.BuiltinMethodType,
        )
    )


def saml2_handler(session, request, config_filename=None, entityid=None):
    config_filename = config_filename or os.path.join(
        request.folder, "private", "sp_conf"
    )
    client = Saml2Client(config_file=config_filename)
    if not entityid:
        idps = client.metadata.with_descriptor("idpsso")
        entityid = list(idps.keys())[0]
    bindings = [BINDING_HTTP_REDIRECT, BINDING_HTTP_POST]
    binding, destination = client.pick_binding(
        "single_sign_on_service", bindings, "idpsso", entity_id=entityid
    )
    if request.env.request_method == "GET":
        binding = BINDING_HTTP_REDIRECT
    elif request.env.request_method == "POST":
        binding = BINDING_HTTP_POST
    if not request.vars.SAMLResponse:
        req_id, req = client.create_authn_request(
            destination, binding=BINDING_HTTP_POST
        )
        relay_state = web2py_uuid().replace("-", "")
        session.saml_outstanding_queries = {req_id: request.url}
        session.saml_req_id = req_id
        http_args = client.apply_binding(
            binding, str(req), destination, relay_state=relay_state
        )
        return {"url": dict(http_args["headers"])["Location"]}
    else:
        relay_state = request.vars.RelayState
        req_id = session.saml_req_id
        unquoted_response = request.vars.SAMLResponse
        res = {}
        try:
            data = client.parse_authn_request_response(
                unquoted_response, binding, session.saml_outstanding_queries
            )
            res["response"] = data if data else {}
        except Exception as e:
            import traceback

            res["error"] = traceback.format_exc()
        return res


class Saml2Auth(object):
    def __init__(
        self,
        config_file=None,
        maps=dict(
            username=lambda v: v[
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn"
            ][0],
            email=lambda v: v[
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn"
            ][0],
            user_id=lambda v: v[
                "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn"
            ][0],
        ),
        logout_url=None,
        change_password_url=None,
        entityid=None,
    ):
        self.config_file = config_file
        self.maps = maps

        # URL for redirecting users to when they sign out
        self.saml_logout_url = logout_url

        # URL to let users change their password in the IDP system
        self.saml_change_password_url = change_password_url

        # URL to specify an IDP if using federation metadata or an MDQ
        self.entityid = entityid

    def login_url(self, next="/"):
        d = saml2_handler(current.session, current.request, entityid=self.entityid)
        if "url" in d:
            redirect(d["url"])
        elif "error" in d:
            redirect(URL("default", "index"))
        elif "response" in d:
            # a['assertions'][0]['attribute_statement'][0]['attribute']
            # is list of
            # {'name': 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname', 'name_format': None, 'text': None, 'friendly_name': None, 'attribute_value': [{'text': 'CAA\\dev-mdp', 'extension_attributes': "{'{http://www.w3.org/2001/XMLSchema-instance}type': 'xs:string'}", 'extension_elements': []}], 'extension_elements': [], 'extension_attributes': '{}'}
            try:
                attributes = (
                    d["response"].assertions[0].attribute_statement[0].attribute
                )
            except:
                attributes = d["response"].assertion.attribute_statement[0].attribute
            current.session.saml2_info = dict(
                (a.name, [i.text for i in a.attribute_value]) for a in attributes
            )
        return next

    def logout_url(self, next="/"):
        current.session.saml2_info = None
        current.session.auth = None
        self._SAML_logout()
        return next

    def change_password_url(self, next="/"):
        self._SAML_change_password()
        return next

    def get_user(self):
        user = current.session.saml2_info
        if user:
            d = {"source": "web2py saml2"}
            for key in self.maps:
                d[key] = self.maps[key](user)
            return d
        return None

    def _SAML_logout(self):
        """
        exposed SAML.logout()
        redirects to the SAML logout page
        """
        redirect(self.saml_logout_url)

    def _SAML_change_password(self):
        redirect(self.saml_change_password_url)
