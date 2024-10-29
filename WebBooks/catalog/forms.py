from django import forms
from datetime import date
from django.forms import ModelForm
from .models import Book

class AuthorsForm(forms.Form):
 first_name = forms.CharField(label="Имя автора")
 last_name = forms.CharField(label="Фамилия автора")
 widget=forms.widgets.DateInput(attrs={'type': 'date'})
 widget=forms.widgets.DateInput(attrs={'type': 'date'})

 class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'language', 'author', 'summary', 'isbn']
labels = {' summary ': ('Аннотация'), }
help_texts = {' summary ': ('Не более 1000 символов'), }

class UserForm(forms.Form):
 email = forms.EmailField(label="Электронный адрес",
 help_text="Обязательный символ - @")