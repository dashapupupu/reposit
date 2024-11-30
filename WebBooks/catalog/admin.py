from django.contrib import admin
from .models import Author, Book, Genre, Language, Publisher, Status, BookInstance
from django.utils.html import format_html

class AuthorAdmin (admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'photo')
    fields = ['last_name', 'first_name', ('date_of_birth', 'photo')]
    readonly_fiedls = ["show_photo"]
    def show_photo(self, obj):
        return format_html (
            f'<img src="{obj.photo.url}" style = "max-height: 100px">'
        )
        show_photo.short_description = 'Фото'
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author', 'show_photo')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]
    readonly_fields = ['show_photo']

    def show_photo(self, obj):
        return format_html('<img src="{}" style="max-height: 100px">'.format(obj.photo.url))
    show_photo.short_description = 'Обложка'

    def display_author(self, obj):
        return obj.author.name

# Регистрируем класс BookInstanceAdmin для экземпляров книг  
class BookInstanceAdmin(admin.ModelAdmin): 
    list_display = ('book', 'status', 'borrower', 'due_back', 'id') 
    list_filter = ('book', 'status') 
    fieldsets = (('Экземпляр книги', {'fields': ('book', 'inv_nom')}), ('Статус и окончание его действия', {'fields': ('status', 'due_back', 'borrower')}),)
admin.site.register(BookInstance)
admin.site.register(Genre) 
admin.site.register(Language) 
admin.site.register(Publisher) 
admin.site.register(Status)
admin.site.register(Book)


# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name')
#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]



# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'genre', 'language', 'display_author')
#     list_filter = ('genre', 'author')
#     inlines = [BooksInstanceInline]


# class BookInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('book', 'status')
#     fieldsets = (
#         (None, {'fields': ('book', 'imprint', 'inv_nom')}),
#         ('Availability', {'fields': ('status', 'due_back', 'borrower')}),
#     )
#     list_display = ('book', 'status', 'borrower', 'due_back', 'id')
#     list_filter = ('status', 'due_back')


# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book, BookAdmin)
# admin.site.register(BookInstance, BookInstanceAdmin)
# admin.site.register(Genre)
# admin.site.register(Language)
# admin.site.register(Publisher)
# admin.site.register(Status)