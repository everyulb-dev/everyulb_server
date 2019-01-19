from django.conf.urls import url
from .contollers import ListCustomers
urlpatterns = [
    url(r'^$',ListCustomers.as_view(),name='customer_list')
]