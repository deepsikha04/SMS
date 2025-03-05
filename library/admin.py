from django.contrib import admin
from .models import Book, Transaction, Member

admin.site.register(Book)
admin.site.register(Transaction)
admin.site.register(Member)
