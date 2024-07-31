from django.urls import path
from watermark_app.views import *

app_name = "watermark_app"

urlpatterns = [
    path('', index_view, name='home'),
]
