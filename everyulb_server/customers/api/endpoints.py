from django.conf.urls import url
from .contollers import ListCreateCustomers,RetrieveUpdateDestroyCustomer

urlpatterns = [
    url(r'^$',ListCreateCustomers.as_view(),name='customer_list'),
    url(r'(?P<pk>\d+)/$',RetrieveUpdateDestroyCustomer.as_view(),name='customer_details'),
]