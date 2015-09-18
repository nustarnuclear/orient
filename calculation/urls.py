from django.conf.urls import url
from calculation import views
from calculation.views import *
urlpatterns = [
    url(r'^base_fuels/$', views.BaseFuel_list),
]