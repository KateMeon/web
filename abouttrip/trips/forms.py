from django import forms
from .models import Category, Voucher
from django.core.validators import MinLengthValidator, MaxLengthValidator


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
