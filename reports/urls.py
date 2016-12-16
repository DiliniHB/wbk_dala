from django.conf.urls import url

from . import views

app_name = 'reports'

urlpatterns = [
    url(r'^index_report$', views.index_report, name='index_report'),
    url(r'^index_chart$', views.index_chart, name='index_chart'),
    url(r'^chart_tabel8$', views.chart_tabel8, name='chart_tabel8'),
    url(r'^chart_tabel9$', views.chart_tabel9, name='chart_tabel9'),
    url(r'^chart_tabel10$', views.chart_tabel10, name='chart_tabel10'),
    url(r'^health_summery_damageloss_dis_report$', views.health_summery_damageloss_dis_report, name='health_summery_damageloss_dis_report'),
    url(r'^health_summery_damageloss_national_report$', views.health_summery_damageloss_national_report, name='health_summery_damageloss_national_report'),
    url(r'^health_summery_damageloss_province_report$', views.health_summery_damageloss_province_report, name='health_summery_damageloss_province_report')

    
]
