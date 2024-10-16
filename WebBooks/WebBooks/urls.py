"""
URL configuration for WebBooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.urls import re_path
from catalog import views

urlpatterns = [
 path('', views.index, name='index'),
 path('authors_add/', views.authors_add, name='authors_add'),
 path('admin/', admin.site.urls),
 path('accounts/', include('django.contrib.auth.urls')),
 re_path(r"^books/$", views.BookListView.as_view(), name='books'),
 re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
 re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
 re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
 path('edit1/<int:id>/', views.edit1, name='edit1'),
 path('create/', views.create, name='create'),
 path('delete/<int:id>/', views.delete, name='delete'),
 re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
 re_path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
 re_path(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),






 path('start1/', views.start1, name='start1'),
 path('colorbg/', views.colorbg, name='colorbg'),
 path('colortext/', views.colortext, name='colortext'),
 path('colortextbg/', views.colortextbg, name='colortextbg'),
 path('space1/', views.space1, name='space1'),
 path('space2/', views.space2, name='space2'),
 path('space3/', views.space3, name='space3'),
 path('aligment1/', views.aligment1, name='aligment1'),
 path('aligment2/', views.aligment2, name='aligment2'),
 path('border1/', views.border1, name='border1'),
 path('border2/', views.border2, name='border2'),
 path('bordercolor/', views.bordercolor, name='bordercolor'),
 path('borderradius/', views.borderradius, name='borderradius'),
 path('borderradius1/', views.borderradius1, name='borderradius1'),
]
#делаю  репаф потому что url убрали(( цитирую:
 #django.conf.urls.url() was deprecated in Django 3.0, and is removed in Django 4.0+.\
