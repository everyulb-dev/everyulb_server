from django.conf.urls import url
from .contollers import ListCreateMap, RetrieveUpdateDestroyMap

urlpatterns = [
    url(r'^$',ListCreateMap.as_view(),name='map_list'),
    url(r'(?P<pk>\d+)/$',RetrieveUpdateDestroyMap.as_view(),name='map_details'),
]