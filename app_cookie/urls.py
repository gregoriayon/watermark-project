from django.urls import path
from app_cookie.views import *

app_name = "app_cookie"

urlpatterns = [
    path('set/', set_cookie_view, name='set-cookie-view'),
    path('get/', get_cookie_view, name='get-cookie-view'),
    path('del/', delete_cookie_view, name='del-cookie-view'),
]
