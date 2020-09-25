from django.contrib import admin
from .models import Projects

admin.site.site_header = "Portfolio Admin"


@admin.register(Projects)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title']
