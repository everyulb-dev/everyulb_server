from django.conf.urls import url
from .contollers import ListCreateVendors, RetrieveUpdateDestroyVendors

urlpatterns = [
    url(r'^$',ListCreateVendors.as_view(),name='vendors_list'),
    url(r'(?P<pk>\d+)/$',RetrieveUpdateDestroyVendors.as_view(),name='vendors_details'),
]