from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from tinymce.widgets import TinyMCE
from django.db import models

class TutorailAdmin(admin.ModelAdmin):
    fields = ['title', 
            'published_date',
            'tutorial_content']

    fieldsets = [
        ('Title/date', {"fields":['title','published_date']}),
        ("URL", {"fields":['tutorial_slug']}),
        ("Series", {"fields":['tutorial_series']}),
        ("Content", {"fields":['tutorial_content']}),

    ]

    formfield_overrides = {
        models.TextField: {'widget' : TinyMCE()}
    }


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial)