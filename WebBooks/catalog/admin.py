from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language, Publisher, Status

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'inv_nom')}),
        ('Availability', {'fields': ('status', 'due_back', 'borrower')}),
    )
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)