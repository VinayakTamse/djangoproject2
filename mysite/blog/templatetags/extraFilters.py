from django import template

register = template.Library()

@register.filter(name='get_key_val')
def get_key_val(dict, key):
    return dict.get(key)

@register.filter(name="get_dict_length")
def get_dict_length(dict):

    return len(dict)