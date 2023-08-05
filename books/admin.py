from django.contrib import admin

from books.models import Book


@admin.register(Book)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_on')
