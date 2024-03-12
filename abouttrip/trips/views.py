from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.shortcuts import render

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name':
            'add_page'},
        {'title': "Обратная связь", 'url_name':
            'contact'},
        {'title': "Войти", 'url_name': 'login'}]

data_db = [
    {'id': 1, 'title': 'Россия', 'content':
        '''<h1>Россия</h1>Путешествия по России могут представляться
         не такими экзотическими, как туры в другие страны, но они обладают
          собственным очарованием и уникальностью. Исследование родной страны 
          может привнести новые эмоции и впечатления, расширить кругозор и позволить
           узнать много интересного о местной истории, культуре и обычаях.''',
     'is_published': True},
    {'id': 2, 'title': 'Египет', 'content':
        '''<h1>Египет</h1>Египет – страна в Северной Африке, популярное 
        направление отдыха у российских туристов круглый год. Страна, где 
        можно совместить пляжный релакс с экскурсиями к историческим
         достопримечательностям и дайвингом.''', 'is_published': False},
    {'id': 3, 'title': 'Турция', 'content':
        '''<h1>Турция</h1> Турция — это больше, чем страна для пляжного 
        отдыха и отелей Аll inclusive, это также страна с богатой природой
         и выгодным географическим положением. Расположенная между европейским
          и азиатским континентами, воссоединила в себе множество культур,
           предлагающих путешественникам испытать целый спектр эмоций.''', 'is_published': True},
]

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
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db,
            'cat_selected': 0,
            }
    return render(request, 'abouttrip/index.html', context=data)


def about(request):
    return render(request, 'abouttrip/about.html',
                  {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id ={post_id}")


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
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'abouttrip/index.html',
                  context=data)
