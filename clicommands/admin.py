from django.contrib import admin

# Register your models here.

from .models import Command

class CommandAdmin(admin.ModelAdmin):
    list_display = ('id','opmode','command','environment','get_tags','cmd_date','owner','is_published')
    list_display_links = ('id', 'command')
    list_filter = ('tags','opmode','environment','cmd_date','is_published',)
    list_editable = ('is_published',)

    def get_tags(self,obj):
        return ", ".join(tag for tag in obj.tags.names())


admin.site.register(Command,CommandAdmin)