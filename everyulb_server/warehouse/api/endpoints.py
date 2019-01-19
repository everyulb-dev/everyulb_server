from django.conf.urls import url
from .contollers import ListCreateWarehouse, RetrieveUpdateDestroyWarehouse

urlpatterns = [
    url(r'^$',ListCreateWarehouse.as_view(),name='warehouse_list'),
    url(r'(?P<pk>\d+)/$',RetrieveUpdateDestroyWarehouse.as_view(),name='warehouse_details'),
]