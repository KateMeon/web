from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from trips.models import Trips, Category, TagPost, UploadFiles
from trips.forms import AddPostForm, UploadFileForm
import uuid

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name':
            'add_page'},
        {'title': "Обратная связь", 'url_name':
            'contact'},
        {'title': "Войти", 'url_name': 'login'}]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# Create your views here.
def index(request):
    return render(request, 'abouttrip/index.html', context=data)


class TripsHome(TemplateView):
    template_name = 'abouttrip/index.html'
    # extra_context = {'title': 'Главная страница',
    #                  'menu': menu,
    #                  'posts': Trips.published.all().select_related('cat'),
    #                  'cat_selected': 0,
    #                  }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        context['posts'] = Trips.published.all().select_related('cat')
        context['cat_selected'] = int(self.request.GET.get('cat_id', 0))
        return context


def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    return render(request, 'abouttrip/about.html',
                  {'title': 'О сайте', 'menu': menu, 'form': form})


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


class AddPage(View):
    def get(self, request):
        form = AddPostForm()
        return render(request, 'abouttrip/addpage.html',
                      {'menu': menu, 'title': 'Добавление статьи', 'form': form})

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'abouttrip/addpage.html',
                      {'menu': menu, 'title': 'Добавление статьи', 'form': form})


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
