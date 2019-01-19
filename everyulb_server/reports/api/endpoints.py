from django.conf.urls import url
from .contollers import ListCreateReport, RetrieveUpdateDestroyReport

urlpatterns = [
    url(r'^$',ListCreateReport.as_view(),name='report_list'),
    url(r'(?P<pk>\d+)/$',RetrieveUpdateDestroyReport.as_view(),name='report_details'),
]