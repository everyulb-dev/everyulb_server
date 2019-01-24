from django.conf.urls import url
from .contollers import ListCreateComponent, RetrieveUpdateDestroyComponent, GetProjectComponent, GetComponentTasks

urlpatterns = [
    url(r'^$',ListCreateComponent.as_view(),name='component_list'),
    url(r'(?P<pk>\d+)/$',RetrieveUpdateDestroyComponent.as_view(),name='component_details'),
    url(r'getprojectcomponents/$', GetProjectComponent.as_view(), name='project_components'),
    url(r'(?P<pk>\d+)/getcomponenttasks/$', GetComponentTasks.as_view(), name='component_tasks_details')
]