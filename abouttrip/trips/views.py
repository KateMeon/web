from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.shortcuts import render
from trips.models import Trips, Category, TagPost

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name':
            'add_page'},
        {'title': "Обратная связь", 'url_name':
            'contact'},
        {'title': "Войти", 'url_name': 'login'}]


# cats_db = [
#     {'id': 1, 'name': 'По России'},
#     {'id': 2, 'name': 'По миру'},
#     {'id': 3, 'name': 'Путеводители'},
# ]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# Create your views here.
def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': Trips.published.all(),
            'cat_selected': 0,
            }
    return render(request, 'abouttrip/index.html', context=data)


def about(request):
    return render(request, 'abouttrip/about.html',
                  {'title': 'О сайте', 'menu': menu})


def show_post(request, post_slug):
    post = get_object_or_404(Trips, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'abouttrip/post.html',
                  context=data)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponse('<h1>Страница не найдена</h1>')


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Trips.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'abouttrip/index.html',
                  context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Trips.Status.PUBLISHED)
    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }
    return render(request, 'abouttrip/index.html', context=data)
