from django.conf.urls import url
from calculation import views
from calculation.views import *
urlpatterns = [
    url(r'^base_fuels/$', views.BaseFuel_list),
    url(r'^(?P<plantname>.+?)/unit(?P<unit_num>[1-4])/cycle(?P<cycle_num>[0-9]+)/$', views.BaseCore_detail),
]