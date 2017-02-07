from django import template

register = template.Library()

@register.filter
def get_range(num):
    """Return the list range(num) to loop over."""

    return range(num)