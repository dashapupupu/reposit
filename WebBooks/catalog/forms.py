from django import forms
from datetime import date
from django.forms import ModelForm
from .models import Book
from django.shortcuts import render


class UserForm(forms.Form):
    email = forms.EmailField(label="Электронный адрес", max_length=50)
    def clean_email(self):
        email = self.cleaned_data['email']
        if "@" not in email:
            raise forms.ValidationError("Неправильный формат email. Обязателен символ @.")
        return email

class AuthorsForm(forms.Form):
 first_name = forms.CharField(label="Имя автора")
 last_name = forms.CharField(label="Фамилия автора")
 widget=forms.widgets.DateInput(attrs={'type': 'date'})

class BookModelForm(forms.ModelForm): 
    class Meta: 
        model = Book 
        fields = '__all__'

# форма для добавления в БД новых авторов 
class Form_add_author(forms.Form): 
    first_name = forms.CharField(label="Имя автора") 
    last_name = forms.CharField(label="Фамилия автора") 
    date_of_birth = forms.DateField( 
    label="Дата рождения", 
    initial=format(date.today()), 
    widget=forms.widgets.DateInput(attrs={'type': 'date'})) 
    about = forms.CharField(label="Сведения об авторе", 
    widget=forms.Textarea) 
    photo = forms.ImageField(label="Фото автора")
