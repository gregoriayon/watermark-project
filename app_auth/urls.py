from django.urls import path
from app_auth.views import login_view


app_name = "app_auth"

urlpatterns = [
    path('login/', login_view, name='login'),
]