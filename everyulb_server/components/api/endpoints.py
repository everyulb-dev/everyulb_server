from django.conf.urls import url
from .contollers import ListCreateComponent, RetrieveUpdateDestroyComponent

urlpatterns = [
    url(r'^$',ListCreateComponent.as_view(),name='component_list'),
    url(r'(?P<pk>\d+)/$',RetrieveUpdateDestroyComponent.as_view(),name='component_details'),
]