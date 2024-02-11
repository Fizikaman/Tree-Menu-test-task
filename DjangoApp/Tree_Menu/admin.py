from django.contrib import admin
from .models import TreeMenuBar, CategoryMenu


class CategoryInLine(admin.TabularInline):
    """Отображение категорий в админке"""
    model = TreeMenuBar
    prepopulated_fields = {"url": ("title",)}


@admin.register(CategoryMenu)
class CategoryMenuAdmin(admin.ModelAdmin):
    """Создание админ панели для категории"""
    list_display = ('name',)
    inlines = (CategoryInLine,)


@admin.register(TreeMenuBar)
class TreeMenuAdmin(admin.ModelAdmin):
    """Создание админ интерфейса для модели TreeMenu"""
    prepopulated_fields = {"url": ("title",)}
    list_display = ('title', 'url', 'parent', 'category')
