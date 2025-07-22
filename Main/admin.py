from django.contrib import admin
from .models import Book, Category


# Register your models here.

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    pass