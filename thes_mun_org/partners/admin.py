from django.contrib import admin
from .models import Partner


# Register your models here.

class PartnerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Position in Site', {'fields': ['position']}),
        ('Content', {'fields': ['image', 'content']})
    ]
    list_display = ('name', 'position')
    search_fields = ['name']


admin.site.register(Partner, PartnerAdmin)
