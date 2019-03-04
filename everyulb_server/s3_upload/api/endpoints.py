from django.conf.urls import url
from .contollers import UploadFileS3, RetrieveDestroyFileS3, force_download, set_file_status

urlpatterns = [
    url(r'uploads/$', UploadFileS3.as_view(), name='uploadfiles3'),
    url(r'uploads/(?P<id>\d+)/$', RetrieveDestroyFileS3.as_view(), name='retrieve_destroy_files'),
    url(r'uploads/(?P<id>\d+)/download/$', force_download, name='force_download'),
    url(r'uploads/(?P<id>\d+)/set_status/$', set_file_status, name='set_file_status'),

]