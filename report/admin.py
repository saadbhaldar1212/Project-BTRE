from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from report.models import Report

from .models import Report

from realtors.admin import RealtorAdmin


class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "realtor",
        "contact",
        "listings",
    )
    search_fields = ("name",)
    list_per_page = 25


admin.site.register(Report, ReportAdmin)
