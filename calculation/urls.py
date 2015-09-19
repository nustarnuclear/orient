from django.conf.urls import url
from calculation import views
from calculation.views import *
urlpatterns = [
    url(r'^base_component/$', views.BaseFuel_list),
    url(r'^basecore/(?P<plantname>.+?)/unit(?P<unit_num>[1-4])/cycle(?P<cycle_num>[0-9]+)/$', views.BaseCore_detail),
    url(r'^loading_pattern/(?P<plantname>.+?)/unit(?P<unit_num>[1-4])/$', views.LoadingPattern_list),
]