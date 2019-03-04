"""everyulb_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import refresh_jwt_token
from everyulb_server import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),

    url(r'^api/v1/auth/', include('rest_auth.urls')),
    url(r'^api/v1/auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/auth/token-refresh/', refresh_jwt_token),


    url(r'^api/v1/customers/', include(('customers.api.endpoints', 'customers'), namespace='customers')),
    url(r'^api/v1/projects/', include(('projects.api.endpoints', 'projects'), namespace='projects')),
    url(r'^api/v1/components/', include(('components.api.endpoints', 'components'), namespace='components')),
    url(r'^api/v1/maps/', include(('maps.api.endpoints', 'maps'), namespace='maps')),
    url(r'^api/v1/profiles/', include(('profiles.api.endpoints', 'profiles'), namespace='profiles')),
    url(r'^api/v1/reportcollections/', include(('reportcollections.api.endpoints', 'reportcollections'), namespace='reportcollections')),
    url(r'^api/v1/reports/', include(('reports.api.endpoints', 'reports'), namespace='reports')),
    url(r'^api/v1/tasks/', include(('tasks.api.endpoints', 'tasks'), namespace='tasks')),
    url(r'^api/v1/vendors/', include(('vendors.api.endpoints', 'vendors'), namespace='vendors')),
    url(r'^api/v1/warehouse/', include(('warehouse.api.endpoints', 'warehouse'), namespace='warehouse')),
    url(r'^api/v1/s3_upload/', include(('s3_upload.api.endpoints', 's3_upload'), namespace='s3_upload')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_title = 'EveryULB Super Admin'
admin.site.site_header = 'EveryULB Admin'
admin.site.index_title = 'EveryULB'