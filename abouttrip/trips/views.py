from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, \
    UpdateView, DeleteView

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

class TripsHome(ListView):
    model = Trips
    template_name = 'abouttrip/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        context['cat_selected'] = int(self.request.GET.get('cat_id', 0))
        return context

    def get_queryset(self):
        return Trips.published.all().select_related('cat')


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


class AddPage(CreateView):
    model = Trips
    template_name = 'abouttrip/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': 'Добавление статьи',
    }
    fields = '__all__'


class UpdatePage(UpdateView):
    model = Trips
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'abouttrip/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': 'Редактирование статьи',
    }


class DeletePage(DeleteView):
    model = Trips
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'abouttrip/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': 'Удаление статьи',
    }

def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponse('<h1>Страница не найдена</h1>')


# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     posts = Trips.published.filter(cat_id=category.pk)
#     data = {
#         'title': f'Рубрика: {category.name}',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': category.pk,
#     }
#     return render(request, 'abouttrip/index.html',
#                   context=data)


class TripsCategory(ListView):
    template_name = 'abouttrip/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Рубрика - ' + cat.name
        context['menu'] = menu
        context['cat_selected'] = cat.id
        return context

    def get_queryset(self):
        return Trips.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')


# def show_post(request, post_slug):
#     post = get_object_or_404(Trips, slug=post_slug)
#     data = {
#         'title': post.title,
#         'menu': menu,
#         'post': post,
#         'cat_selected': 1,
#     }
#     return render(request, 'abouttrip/post.html',
#                   context=data)


class ShowPost(DetailView):
    model = Trips
    template_name = 'abouttrip/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Trips.published, slug=self.kwargs[self.slug_url_kwarg])


class TagPostList(ListView):
    template_name = 'abouttrip/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = 'Тег: ' + tag.tag
        context['menu'] = menu
        context['cat_selected'] = None
        return context

    def get_queryset(self):
        return Trips.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')
