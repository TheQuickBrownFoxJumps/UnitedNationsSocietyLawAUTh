from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Event


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title', 'slug']}),
        ('Author', {'fields': ['author']}),
        ('Publication Date', {'fields': ['date']}),
        ('Content', {'fields': ['image', 'content']})
    ]
    list_display = ('title', 'author', 'date', )
    list_filter = ['author', 'date']
    search_fields = ['title']


admin.site.register(Event, EventAdmin)
