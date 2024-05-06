from django.contrib import admin
from .models import Category, Author, News
# Register your models here.

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(News)