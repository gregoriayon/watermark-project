from django.urls import path
from app_deep_query.views import QueryView

app_name = "app_deep_query"

urlpatterns = [
    path('', QueryView.as_view(), name='query-view'),
]