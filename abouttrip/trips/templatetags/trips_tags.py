from django import template
import trips.views as views
from trips.models import Category, TagPost
from django.db.models import Count

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('abouttrip/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Category.objects.annotate(total=Count("posts")).filter(total__gt=0)
    return {"cats": cats, "cat_selected": cat_selected_id}

    # cats = Category.objects.all()
    # return {"cats": cats, "cat_selected": cat_selected_id}


@register.inclusion_tag('abouttrip/list_tags.html')
def show_all_tags():
    return {"tags": TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)}
