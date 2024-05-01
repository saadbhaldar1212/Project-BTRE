from django.contrib import admin

from .models import Report


@admin.register(Report)
class RealtorAdmin(admin.ModelAdmin):
    name_display = ("name",)
