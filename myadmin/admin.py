from django.contrib import admin
from .models import Notices

admin.site.site_header = 'Notice Hub Webapp'
admin.site.index_title = 'My Admin Panel'

# Register your models here.

class shownotice(admin.ModelAdmin):
    list_display = ['subject', 'description', 'created_at', 'updated_at']

admin.site.register(Notices, shownotice)