from django.contrib import admin

from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    list_display = ('name', 'parent', 'url')
    list_filter = ('name', 'parent')
    search_fields = ('name',)
    prepopulated_fields = {'url': ('name',)}
