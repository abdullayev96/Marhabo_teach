from django.contrib import admin
from .models import Article, Category

# Register your models here.

class ArticlesCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Article)
admin.site.register(Category,ArticlesCategory)