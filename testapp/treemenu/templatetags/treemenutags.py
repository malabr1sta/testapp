from django import template
from treemenu.models import Category
from typing import List, Dict
from django.shortcuts import get_object_or_404

HREF = '''
<ul>
  <a href="./%s">
    <li>%s</li>
  </a>
'''

register = template.Library()


def get_menu(menu: List[Category], item: Category) -> dict:
    """Функция возвращет словарь с узлами и их потомками,
    которые надо вывести на страницы."""

    if item is None:
        return {'/': menu.filter(parent=None)}
    children = item.get_children()
    menu_dict = get_menu(menu, item.parent)
    menu_dict[item.title] = children
    return menu_dict


def get_html(menu: Dict[str, List[Category]],
             dir: List[Category]) -> str:
    """Функция формирует html код для выбранного пункта меню."""

    html_code = ''
    for node in dir:
        html_code += HREF % (node.title, node.title)
        children = menu.pop(node.title, False)
        if children:
            html_code += get_html(menu, children)
        html_code += '</ul>'
    return html_code


@register.simple_tag()
def draw_menu(name_menu):
    menu_list = Category.objects.select_related('parent').all()
    if name_menu is None:
        item = name_menu
    else:
        item = get_object_or_404(menu_list, title=name_menu)
    dict_menu = get_menu(menu_list, item)
    roots_dir = dict_menu.pop('/')
    return get_html(dict_menu, roots_dir)
