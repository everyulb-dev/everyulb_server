from django.conf.urls import url
from .contollers import ListCreateProject,RetrieveUpdateDestroyProject, GetProjectDetails

urlpatterns = [
    url(r'^$',ListCreateProject.as_view(),name='project_list'),
    url(r'(?P<pk>\d+)/$',RetrieveUpdateDestroyProject.as_view(),name='project_details'),
    url(r'getprojectdetails', GetProjectDetails.as_view(), name='full_project_details'),
]