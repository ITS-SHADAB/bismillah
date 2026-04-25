from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Page, MenuItem


# Create your views here.


def page_view(request, lang, slug):
    page = get_object_or_404(Page, slug=slug)
    menu = MenuItem.objects.all().order_by('order')

    if lang == 'ur':
        context = {
            'title': page.title_ur,
            'content': page.content_ur,
            'menu': menu,
            'lang': 'ur'
        }
    else:
        context = {
            'title': page.title_en,
            'content': page.content_en,
            'menu': menu,
            'lang': 'en'
        }

    return render(request, 'page.html', context)