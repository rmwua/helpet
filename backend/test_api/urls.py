from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
]
