# -*- coding: utf-8 -*-
"""admin.py: Central Messages"""

from __future__ import unicode_literals

from .models import CentralMessage
from django.contrib import admin


class CentralMessageAdmin(admin.ModelAdmin):
    list_display = ['level', 'user', 'message', 'created', 'generated']
    # These don't make sense to edit
    exclude = ('read', 'generated', 'generated_on')
    actions = ['generate']

    def generate(self, request, queryset):
        for x in queryset:
            x.generate()
    generate.short_description = "Generate CentralUserMessages for all users."

admin.site.register(CentralMessage, CentralMessageAdmin)
