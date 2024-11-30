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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 path('', views.index, name='index'),
#  path('catalog/', include('catalog.urls')), 
 path('authors_add/', views.authors_add, name='authors_add'),
 path('admin/', admin.site.urls),
 path('accounts/', include('django.contrib.auth.urls')),
 path('books/', views.BookListView.as_view(), name='books'),
 
 path('books/', views.BookListView.as_view(), name='books-list'), 
 path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
# re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
 re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
 re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
 path('edit1/<int:id>/', views.edit1, name='edit1'),
 path('create/', views.create, name='create'),
 path('delete/<int:id>/', views.delete, name='delete'),
 re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
 path('book/update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'), 
 path('book/delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'), 
 path('publisher/', views.publisher_list, name='publisher_list'),
 path('books/', views.BookListView.as_view(), name='books-list'), 
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#делаю  репаф потому что url убрали(( цитирую:
 #django.conf.urls.url() was deprecated in Django 3.0, and is removed in Django 4.0+.\
