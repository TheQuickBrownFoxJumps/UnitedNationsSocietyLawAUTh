from django.contrib import admin
from .models import New


# Register your models here.

class NewAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Author', {'fields': ['author']}),
        ('Publication Date', {'fields': ['date']}),
        ('Content', {'fields': ['href_url', 'image', 'image_detail', 'content']})
    ]
    list_display = ('title', 'author', 'date', )
    list_filter = ['author', 'date']
    search_fields = ['title']


admin.site.register(New, NewAdmin)
