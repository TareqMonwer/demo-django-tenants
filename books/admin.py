from django_tenants.admin import TenantAdminMixin

from django.contrib import admin

from books.models import Book


@admin.register(Book)
class PublisherAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'author', 'publisher', 'category', 'created_on')
