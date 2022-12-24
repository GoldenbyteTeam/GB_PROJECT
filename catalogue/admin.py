from django.contrib import admin

# Register your models here.

from .models import Catalogue,Keywords,Category

class CatalogueAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','is_published')
    list_display_links = ('id', 'title')
    list_filter = ('category','is_published',)
    list_editable = ('is_published',)

class KeywordAdmin(admin.ModelAdmin):
    list_display = ('id','name','keywords')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')


admin.site.register(Catalogue,CatalogueAdmin)
admin.site.register(Keywords,KeywordAdmin)
admin.site.register(Category,CategoryAdmin)