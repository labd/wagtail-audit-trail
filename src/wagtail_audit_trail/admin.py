from django.contrib import admin

from wagtail_audit_trail import models


@admin.register(models.PageRecord)
class PageRecordAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'page', 'revision']
