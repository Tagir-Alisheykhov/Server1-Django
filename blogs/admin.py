from django.contrib import admin
from .models import BlogEntry, Category


@admin.register(BlogEntry)
class BlogsAdmin(admin.ModelAdmin):
    """Регистрация модели блоговых-записей (статей)"""
    list_display = (
        "id",
        "title",
        "description",
        "preview",
        "created_at",
        "is_publication_attribute",
        "views_counter"
    )
    list_filter = (
        "created_at",
        "views_counter"
    )
    search_fields = (
        "title",
        "description",
        "created_at"
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Регистрация модели категории статей"""
    list_display = ("id", "name")
    search_fields = ("name", "description")
