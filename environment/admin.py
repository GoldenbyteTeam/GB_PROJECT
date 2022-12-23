from django.contrib import admin

# Register your models here.

from .models import Environment

admin.site.register(Environment)