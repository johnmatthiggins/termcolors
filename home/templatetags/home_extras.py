from django import template

register = template.Library()

@register.filter(name="dict_key")
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''

    try:
        if str(k) in d:
            return d[str(k)]
    except TypeError:
        pass

    return getattr(d, str(k))

@register.filter(name="rangeloop")
def rangeloop(start, end=0):
    if end:
        return range(start, end)
    return range(0, start)

@register.filter(name="concat")
def concat(a, b):
    return str(a) + str(b)
