from django.contrib import admin
from .models import Author, Book

# Register your models here.
# 어드민.사이트.등록(Author class)
# 어드민.사이트.등록(Book class)
admin.site.register(Author)
admin.site.register(Book)