from django.shortcuts import render

from .models import Employee, Report


# Create your views here.


def all_reports(request):
    reports = Report.objects.all()
    context = {
        'reports': reports
    }
    return render(request, 'rnumgen/all_reports.html', context)


def report(request, report_no):
    identified_report = Report.objects.get(rnumber=report_no)
    context = {
        'report': identified_report
    }
    return render(request, 'rnumgen/report.html', context)
