from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Voucher, Trips


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 empty_label="Категория не выбрана", label="Категории")
    voucher = forms.ModelChoiceField(queryset=Voucher.objects.all(), required=False,
                                     empty_label="Нет ваучера", label="Ваучер")

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов')
        return title

    class Meta:
        model = Trips
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'voucher', 'tags']
        labels = {'slug': 'URL'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class UploadFileForm(forms.Form):
    file = forms.ImageField(label="Изображение")
