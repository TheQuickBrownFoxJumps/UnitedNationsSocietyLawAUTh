import datetime
from abc import ABC

from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Member, BoardMember, AssociateMember
import string


# Register your models here.
class AlphabetFilter(admin.SimpleListFilter):
    title = 'alphabet'
    parameter_name = 'alphabet'

    def lookups(self, request, model_admin):
        abc = list(string.ascii_lowercase)
        return ((c.upper(), c.upper()) for c in abc)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(name__startswith=self.value())


class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identification', {'fields': ['name', 'surname', 'sex', 'birth_date']}),
        ('Date Created', {'fields': ['init_date']}),
        ('Communication', {'fields': ['mail', 'phone']}),
        ('Education background and MUN experience', {'fields': ['education_background', 'mun_exp_bio']}),
        ('Payment', {'fields': ['payment', 'last_payment_date']}),
    ]

    list_display = ('surname', 'name', 'sex', 'education_background', 'created_years_ago',
                    'payment_status', 'paid_not_paid',)
    list_filter = [AlphabetFilter, 'init_date', 'sex', 'education_background', 'payment']
    search_fields = ['surname', 'name']


class BoardMemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Board Member Role', {'fields': ['role']}),
        ('Identification', {'fields': ['name', 'surname', 'sex']}),
        ('Social Media', {'fields': ['social_url', 'email_url']}),
        ('Profile Pic', {'fields': ['member_pic']}),
        ('Bio', {'fields': ['member_bio']}),
    ]

    list_display = ('role', 'surname', 'name')
    list_filter = [AlphabetFilter, 'role', 'surname', 'sex']
    search_fields = ['surname', 'name']


class AssociateMemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identification', {'fields': ['name', 'surname', 'sex', 'birth_date']}),
        ('Date Created', {'fields': ['init_date']}),
        ('Communication', {'fields': ['mail', 'phone']}),
        ('Education background and MUN experience', {'fields': ['education_background', 'mun_exp_bio']}),
    ]

    list_display = ('surname', 'name', 'sex', 'education_background', 'created_years_ago',)
    list_filter = [AlphabetFilter, 'init_date', 'sex', 'education_background']
    search_fields = ['surname', 'name']


admin.site.register(BoardMember, BoardMemberAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(AssociateMember, AssociateMemberAdmin)
