from django.urls import path, include
from .views import GoogleLoginView, UserRedirectView, FacebookLoginView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register', include('dj_rest_auth.registration.urls')),
    path('google/login/', GoogleLoginView.as_view(), name='google_login'),
    path('facebook/login', FacebookLoginView.as_view(), name='fb_login'),
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect"),
]

