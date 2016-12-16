from django.shortcuts import render
from django.http import HttpResponse


def index(request):   
    return render(request, 'reports/index.html')

def health_summery_damageloss_dis_report(request):   
    return render(request, 'reports/health_summery_damageloss_dis_report.html')

def health_summery_damageloss_national_report(request):   
    return render(request, 'reports/health_summery_damageloss_national_report.html')

def health_summery_damageloss_province_report(request):   
    return render(request, 'reports/health_summery_damageloss_province_report.html')
