from django.contrib import admin

from .models import Book, Author


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"book_slug": ("book_title",)}
    list_display = ("book_title", "book_author", "book_rating")
    list_filter = ("book_rating", "book_author")

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("author_first_name", "author_last_name", "author_is_alive")
    list_filter = ("author_is_alive",)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
