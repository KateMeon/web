from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.shortcuts import render

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
data_db = [
    {'id': 1, 'title': 'Россия', 'content':
        'Информация о путешествиях по России', 'is_published': True},
    {'id': 2, 'title': 'Египет', 'content':
        'Информация о путешествиях по Египту', 'is_published': False},
    {'id': 3, 'title': 'Турция', 'content':
        'Информация о путешествиях по Турции', 'is_published': True},

]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# Create your views here.
def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db,
            }
    return render(request, 'abouttrip/index.html', context=data)


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id ={post_id}")


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
