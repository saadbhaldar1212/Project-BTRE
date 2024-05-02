from django.contrib import admin

from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    name_display = ("name",)
    report_display = ("name", "realtor", "contact", "listing")


# admin.site.register(Report, ReportAdmin)
