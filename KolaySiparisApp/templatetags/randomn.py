from django import template
import random


register = template.Library()

@register.simple_tag(takes_context = True)
def DoRandom(context):
    items = ['success','warning','danger','info', 'danger', 'primary']
    rand_item = items[random.randrange(len(items)-1)]
    return rand_item
