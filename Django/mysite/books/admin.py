from django.contrib import admin
from .models import Book, Comments, Users, Cart

admin.site.register(Book)
admin.site.register(Comments)
admin.site.register(Users)
admin.site.register(Cart)