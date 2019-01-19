from django.conf.urls import url
from .contollers import ListCreateProfile, RetrieveUpdateDestroyProfile

urlpatterns = [
    url(r'^$',ListCreateProfile.as_view(),name='profile_list'),
    url(r'(?P<pk>\d+)/$',RetrieveUpdateDestroyProfile.as_view(),name='profile_details'),
]