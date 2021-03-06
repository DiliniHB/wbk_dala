from django.conf.urls import url
from .import views

app_name = 'dashboard'

urlpatterns = [

    url(r'^dl_health_damagelost_other_medical_facilities$', views.dl_health_damagelost_other_medical_facilities,
        name='dl_health_damagelost_other_medical_facilities'),
    url(r'^dl_save_data$', views.dl_save_data, name='dl_save_data'),
    url(r'^dl_get_data$', views.dl_get_data, name='dl_get_data'),
    url(r'^dl_fetch_edit_data$', views.dl_fetch_edit_data, name='dl_fetch_edit_data'),
    url(r'^fetch_incident_districts$', views.fetch_incident_districts, name='fetch_incident_districts'),
    url(r'^fetch_incident_provinces$', views.fetch_incident_provinces, name='fetch_incident_provinces'),


    #Dileepa and Sachie's
    url(r'^dl_health_summary_sector_district', views.dl_health_summary_sector_district,
        name='dl_health_summary_sector_district'),
    url(r'^dl_health_summary_damage_nationwide', views.dl_health_summary_damage_nationwide,
        name='dl_health_summary_damage_nationwide'),
    # url(r'^dl_save_data$', views.dl_save_data, name='dl_save_data'),
    url(r'^health_damagelost_ministry_helth', views.health_damagelost_ministry_helth,
        name='health_damagelost_ministry_helth'),
    url(r'^health_damagelost_private', views.health_damagelost_private, name='health_damagelost_private'),

]
