from django.template.defaulttags import register
from django import template
register = template.Library()

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_value2(dictionary, key):
    return dictionary[key]