from django.conf.urls import url

from . import views

app_name = 'appauth'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^settings/$', views.displaySettings, name='settings'),
    url(r'^passwordpage/$', views.changePasswordView, name='passwordpage'),
    url(r'^passwordpage/changepassword/$', views.changepassword, name='changepassword'),
    url(r'^settings/update/$', views.updateSettings, name='update_settings'),
    url(r'^forgotpassword/$', views.forgot_password, name='forgotpassword'),
]