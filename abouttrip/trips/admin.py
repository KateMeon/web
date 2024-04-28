from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Trips, Category


# Register your models here.
class VoucherFilter(admin.SimpleListFilter):
    title = 'Статус путешествия'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [('voucher', 'С ваучером'), ('no voucher', 'Без ваучера'), ]

    def queryset(self, request, queryset):
        if self.value() == 'voucher':
            return queryset.filter(voucher__isnull=False)
        elif self.value() == 'no voucher':
            return queryset.filter(voucher__isnull=True)


@admin.register(Trips)
class TripsAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat', 'voucher_info')
    list_display_links = ('title',)
    ordering = ['time_create', 'title']
    list_editable = ('is_published',)
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = [VoucherFilter, 'cat__name', 'is_published']
    fields = ['title', 'slug', 'content', 'post_photo', 'cat', 'voucher', 'tags']
    readonly_fields = ['post_photo']
    prepopulated_fields = {"slug": ("title",)}
    # filter_horizontal = ['tags']
    filter_vertical = ['tags']

    # list_per_page = 5

    @admin.display(description="Изображение")
    def post_photo(self, trip: Trips):
        if trip.photo:
            return mark_safe(f"<img src='{trip.photo.url}' width=50>")
        return "Без фото"

    @admin.display(description="Ваучер")
    def voucher_info(self, trip: Trips):
        if trip.voucher:
            return f"Название ваучера: \"{trip.voucher.name}.\""
        return f"Ваучер отсутствует."

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        queryset.update(is_published=Trips.Status.PUBLISHED)
        count = queryset.update(is_published=Trips.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записи(ей).")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Trips.Status.DRAFT)
        self.message_user(request, f"{count} записи(ей) сняты с публикации!", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
