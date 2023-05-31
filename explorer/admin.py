from django.contrib import admin

# Register your models here.

from .models import Explorer

class ExplorerAdmin(admin.ModelAdmin):
    list_display = ('id','title','awesome_font_logo','url')
    list_display_links = ('id', 'title')

admin.site.register(Explorer,ExplorerAdmin)


