from django.conf.urls import url
from .contollers import CSVToJSON, CSVToJSONId

urlpatterns = [
    url(r'csvtojson/$', CSVToJSON.as_view(), name='CSVToJSON'),
    url(r'csvtojson/(?P<id>\d+)/$', CSVToJSONId.as_view(), name='CSVToJSONId'),

]