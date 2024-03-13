from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.shortcuts import render
from trips.models import Trips

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name':
            'add_page'},
        {'title': "Обратная связь", 'url_name':
            'contact'},
        {'title': "Войти", 'url_name': 'login'}]

cats_db = [
    {'id': 1, 'name': 'По России'},
    {'id': 2, 'name': 'По миру'},
    {'id': 3, 'name': 'Путеводители'},
]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# Create your views here.
def index(request):
    posts = Trips.published.all()
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': posts,
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


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': Trips.published.all(),
        'cat_selected': cat_id,
    }
    return render(request, 'abouttrip/index.html',
                  context=data)
