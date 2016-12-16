from django.shortcuts import render
from django.http import HttpResponse


def index_report(request):   
    return render(request, 'reports/index_report.html')

def index_chart(request):   
    return render(request, 'reports/index_chart.html')

def chart_tabel8(request):   
    return render(request, 'reports/chart_tabel8.html')

def chart_tabel9(request):   
    return render(request, 'reports/chart_tabel9.html')

def chart_tabel10(request):   
    return render(request, 'reports/chart_tabel10.html')

def health_summery_damageloss_dis_report(request):   
    return render(request, 'reports/health_summery_damageloss_dis_report.html')

def health_summery_damageloss_national_report(request):   
    return render(request, 'reports/health_summery_damageloss_national_report.html')

def health_summery_damageloss_province_report(request):   
    return render(request, 'reports/health_summery_damageloss_province_report.html')
