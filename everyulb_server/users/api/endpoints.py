from django.conf.urls import url
from .contollers import CustomUserLogin, CustomUserLogout, CustomUserRegister

urlpatterns = [
    url(r'login/$', CustomUserLogin.as_view(), name='custom_user_login'),
    url(r'logut/$', CustomUserLogout.as_view(), name='custom_user_logout'),
    url(r'login/$', CustomUserRegister.as_view(), name='custom_user_register'),

]