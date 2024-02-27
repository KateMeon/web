from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.shortcuts import render

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# Create your views here.
def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'float': 28.56,
            'lst': [1, 2, 'abc', True],
            'set': {1, 1, 2, 3, 2, 5},
            'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
            'obj': MyClass(10, 20),
            }
    return render(request, 'abouttrip/index.html', context=data)


def about(request):
    return render(request, 'abouttrip/about.html', {'title': 'О сайте', 'menu': menu})


def countries(request, country_id):
    return HttpResponse(f"<h1>Статьи по странам</h1><p>id:{country_id}</p>")


def countries_by_slug(request, country_slug):
    if request.GET:
        print(request.GET)
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по странам</h1><p>Страна:{country_slug}</p>")


def archive(request, year):
    if year > 2024:
        return redirect('home', permanent=True)
    # raise Http404()

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponse('<h1>Страница не найдена</h1>')
