from django.conf.urls import url
from calculation import views
from calculation.views import *
urlpatterns = [
    url(r'^base_component/(?P<plantname>.+?)/$', views.BaseFuel_list),
    url(r'^basecore/(?P<plantname>.+?)/unit(?P<unit_num>[1-4])/$', views.BaseCore_detail),
    url(r'^loading_pattern/(?P<plantname>.+?)/unit(?P<unit_num>[1-4])/$', views.LoadingPattern_list),
    url(r'^egret_task/$',views.generate_egret_task)
]