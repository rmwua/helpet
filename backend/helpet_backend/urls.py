"""
URL configuration for helpet_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, include, re_path

from django.views.generic import RedirectView, TemplateView
from rest_framework.schemas import get_schema_view

import helpet_backend.settings as settings

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(
        url='swagger/',
        permanent=False
    ), name='index'),
    path('swagger/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'../static/openapi-schema.yml'}
    ), name='swagger-ui'),

    path('hello-world/', include('test_api.urls')),
    path('auth/', include('myauth.urls')),
    path('app/chatbot/', include('chatbot.urls')),
    path('app/', include('pets.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
