from django.contrib import admin
from .models import Book, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
