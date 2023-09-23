from django.contrib import admin
from .models import Recipe
from .models import Review

# Register your models here. 
admin.site.register(Recipe)
admin.site.register(Review)