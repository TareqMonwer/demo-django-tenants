from django_tenants.admin import TenantAdminMixin

from django.contrib import admin

from books_platform_shared.models import Category, Publisher


@admin.register(Category)
class CategoryAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'created_on')


@admin.register(Publisher)
class PublisherAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'location')
