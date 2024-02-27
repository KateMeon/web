from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'abouttrip/index.html')


def about(request):
    return render(request, 'abouttrip/about.html')


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
