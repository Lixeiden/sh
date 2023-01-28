from django.contrib import admin
from .models import TelegrafModel


class TelegrafModelAdmin(admin.ModelAdmin):
    list_display = ('uri', 'content', 'created', 'file')
    #list_display_links = ('uri',)
    #list_editable = ('content',)
    list_filter = ('created',)
    search_fields = ('uri', 'content')

admin.site.register(TelegrafModel, TelegrafModelAdmin)
