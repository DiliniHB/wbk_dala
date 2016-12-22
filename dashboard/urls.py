from django.conf.urls import url
from .import views

app_name = 'dashboard'

urlpatterns = [


    url(r'^index$', views.index,name='index'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout', {'next_page': '/admin/login/'}, name='logout'
        ),

]
