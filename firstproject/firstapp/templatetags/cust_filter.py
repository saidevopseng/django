from django import template
register=template.Library()

def first_five_upper(value):
    result=value[:5].upper()
    return result

register.filter('ffu',first_five_upper)