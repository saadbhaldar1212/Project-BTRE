from django.shortcuts import render, get_object_or_404

from .models import Report


def index(request, report_id):

    report = get_object_or_404(Report, pk=report_id)
    context = {"reports": report}
    return render(request, "admin/report.html", context)
