from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'get_children')
    list_display_links = ('title',)


admin.site.register(Category, CategoryAdmin)
