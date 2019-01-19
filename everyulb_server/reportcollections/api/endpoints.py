from django.conf.urls import url
from .contollers import ListCreateReportcollection, RetrieveUpdateDestroyReportcollection

urlpatterns = [
    url(r'^$',ListCreateReportcollection.as_view(),name='reportcollection_list'),
    url(r'(?P<pk>\d+)/$',RetrieveUpdateDestroyReportcollection.as_view(),name='reportcollection_details'),
]