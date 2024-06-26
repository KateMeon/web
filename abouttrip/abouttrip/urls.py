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
from django.conf.urls.static import static
from trips import views
from abouttrip import converters, settings

register_converter(converters.FourDigitYearConverter, "year4")
handler404 = views.page_not_found

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Путешествия по миру"

urlpatterns = [
    path('', views.TripsHome.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    # path('category/<int:cat_id>/', views.show_category, name='category'),
    path('category/<slug:cat_slug>/', views.TripsCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<slug:slug>/', views.DeletePage.as_view(), name='delete_page'),
    path("__debug__/", include("debug_toolbar.urls")),
    path('users/', include("users.urls", namespace="users")),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
