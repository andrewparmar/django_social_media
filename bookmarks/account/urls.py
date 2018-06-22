from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.dashboard, name='dashboard'),

    #login/logout views
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^jello/$', views.jello_world, name='jello'),

    # Old route
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^hello/$', views.hello_world, name='hello')

]