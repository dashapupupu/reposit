from django.contrib import admin
from .models import Author, Book, Genre, Language, Publisher, Status, BookInstance
from django.utils.html import format_html
from django.urls import reverse


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'show_photo')
    fields = ('last_name', 'first_name', 'date_of_birth', 'photo', 'about')
    readonly_fields = ('show_photo',)

    def show_photo(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" style="max-height:100px;">')
        return "Фото отсутствует"
    show_photo.short_description = 'Фото'

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_authors', 'publisher', 'price', 'show_photo')
    list_filter = ('genre', 'author', 'language', 'publisher')
    inlines = [BooksInstanceInline]
    readonly_fields = ('show_photo',)

    def display_authors(self, obj):
        return ', '.join([str(author) for author in obj.author.all()])
    display_authors.short_description = 'Авторы'

    def show_photo(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" style="max-height:1000px;">')
        return "Обложка отсутствует"
    show_photo.short_description = 'Обложка'

    def get_absolute_url(self, obj):
        return reverse('book-detail', args=[str(obj.id)])


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('inv_nom', 'book', 'status', 'borrower', 'due_back')
    list_filter = ('book', 'status', 'due_back')
    fieldsets = (
        (None, {'fields': ('book', 'inv_nom')}),
        ('Status and Due Date', {'fields': ('status', 'due_back', 'borrower')}),
    )

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)
admin.site.register(Author, AuthorAdmin)