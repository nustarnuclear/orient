from django.conf.urls import url
from tragopan import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    #url(r'^$', views.index,name='index'),
    #url(r'^add_material/$', views.add_material,name='add_material'),
    url(r'^element/$', views.ElementViewSet.as_view({'get': 'list'})),
    
    url(r'^fuel_assembly_loading_pattern/$', views.fuel_assembly_loading_pattern_list),
    url(r'^fuel_assembly_loading_patterns/(?P<pk>[0-9]+)/$', views.fuel_assembly_loading_pattern_detail),
    url(r'^(?P<plantname>.+?)/unit(?P<unit_num>[1-4])/cycle(?P<cycle_num>[0-9]+)/$', views.cycle_detail),
    #url(r'^cycles/(?P<pk>[0-9]+)/$', views.CylcleViewSet.as_view({'get': 'retrieve'})),
    
    url(r'^hello_test/$', views.hello_test),
]

urlpatterns = format_suffix_patterns(urlpatterns)