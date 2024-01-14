from django.contrib import admin
from .models import Category,Products,Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Products)
