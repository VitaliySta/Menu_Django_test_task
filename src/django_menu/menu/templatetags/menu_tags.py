from django import template
from django.shortcuts import get_object_or_404

from ..models import Menu

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, name_or_id):

    if isinstance(name_or_id, int):
        menu = get_object_or_404(Menu, pk=name_or_id)
    else:
        menu = get_object_or_404(Menu, name=name_or_id)
    context['menu'] = menu
    current_url = context['request'].path.strip('/')

    if current_url:
        current_menu = Menu.objects.get(url=current_url)
        submenu = current_menu.get_parents() + (current_menu.id,)
        context['submenu'] = submenu

    return context
