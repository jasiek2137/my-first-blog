from ssl import VERIFY_ALLOW_PROXY_CERTS
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.post_list, name='post_list'),
]