"""
URL configuration for abouttrip project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, register_converter, re_path
from trips import views
from abouttrip import converters

register_converter(converters.FourDigitYearConverter, "year4")
handler404 = views.page_not_found
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about),
    path('trips/', include('trips.urls'), name='trips'),
    path('countries/<int:country_id>/', views.countries, name='countries'),
    path('countries/<slug:country_slug>/', views.countries_by_slug, name='countries_id'),
    path('archive/<year4:year>/', views.archive, name='archive'),
    path('post/<int:post_id>/', views.show_post, name='post'),
]
