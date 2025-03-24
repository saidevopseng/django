from django.core.serializers import serialize
import json
from firstapp.models import Employee

class SerializeMixin(object):
    def serialize(self,qs):
        json_data=serialize('json',qs,fields=('eno','ename','eaddr'))
        pdict=json.loads(json_data)
        print(pdict)
        final_list=[]
        for obj in pdict:
            emp_data=obj['fields']
            final_list.append(emp_data)
        json_data=json.dumps(final_list)
        return json_data

from django.http import HttpResponse    
class HttpResponseMixin(object):
    def render_to_http_response(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)
    
    def get_object_by_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
                   
        except Employee.DoesNotExist:
            emp=None
        return emp