from django.shortcuts import render


def index(request):
    template = 'treemenu/menu.html'
    context = {
        'main_menu': None,
    }
    return render(request, template, context=context)


def menu(request, main_menu):
    template = 'treemenu/menu.html'
    context = {
        'main_menu': main_menu,
    }
    return render(request, template, context=context)
