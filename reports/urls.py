from django.conf.urls import url

from . import views

app_name = 'reports'

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^health_summery_damageloss_dis_report$', views.health_summery_damageloss_dis_report, name='health_summery_damageloss_dis_report'),
    url(r'^health_summery_damageloss_national_report$', views.health_summery_damageloss_national_report, name='health_summery_damageloss_national_report'),
    url(r'^health_summery_damageloss_province_report$', views.health_summery_damageloss_province_report, name='health_summery_damageloss_province_report')

    
]
