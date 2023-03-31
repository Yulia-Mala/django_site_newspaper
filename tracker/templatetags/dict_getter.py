from django import template


register = template.Library()


@register.filter
def dict_getter(dictionary, key):
    return dictionary.get(key)
