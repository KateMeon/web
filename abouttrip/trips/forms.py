from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Voucher


# @deconstructible
# class RussianValidator:
#     ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789 - "
#     code = 'russian'
#
#     def __init__(self, message=None):
#         self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел."
#
#     def __call__(self, value):
#         if not (set(value) <= set(self.ALLOWED_CHARS)):
#             raise ValidationError(self.message, code=self.code, params={"value": value})


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=3, label="Заголовок",
                            widget=forms.TextInput(attrs={'class': 'form-input'}),
                            error_messages={'min_length': 'Слишком короткий заголовок',
                                            'requited': 'Необходимо ввести заголовок'})
    slug = forms.SlugField(max_length=255, label="URL",
                           validators=[MinLengthValidator(3, message="Минимум 3 символа"),
                                       MaxLengthValidator(100, message="Максимум 100 символов")])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False,
                              label="Контент")
    is_published = forms.BooleanField(required=False, label="Статус", initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории",
                                 empty_label="Категория не выбрана")
    voucher = forms.ModelChoiceField(queryset=Voucher.objects.all(), required=False, label="Ваучер",
                                     empty_label="Нет ваучера")

    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789 - "
        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError("Должны быть только русские символы, дефис и пробел.")
        return title