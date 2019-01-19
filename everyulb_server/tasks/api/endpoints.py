from django.conf.urls import url
from .contollers import ListCreateTask, RetrieveUpdateDestroyTask

urlpatterns = [
    url(r'^$',ListCreateTask.as_view(),name='task_list'),
    url(r'(?P<pk>\d+)/$',RetrieveUpdateDestroyTask.as_view(),name='task_details'),
]