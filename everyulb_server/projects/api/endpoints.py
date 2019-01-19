from django.conf.urls import url
from .contollers import ListCreateProject,RetrieveUpdateDestroyProject

urlpatterns = [
    url(r'^$',ListCreateProject.as_view(),name='project_list'),
    url(r'(?P<pk>\d+)/$',RetrieveUpdateDestroyProject.as_view(),name='prokecy_details'),
]