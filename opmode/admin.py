from django.contrib import admin

# Register your models here.

from .models import Opmode

class OpmodeAdmin(admin.ModelAdmin):
    list_display = ('id','name','environment')
    list_display_links = ('id', 'name')
    list_filter = ('environment',)

admin.site.register(Opmode,OpmodeAdmin)