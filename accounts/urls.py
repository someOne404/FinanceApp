from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views as core_views


urlpatterns = [
    path('signup/', core_views.signup, name='signup'),
]