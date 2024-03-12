from django.urls import path
from . import views

listCreate = views.ConversationMessagingViewSet.as_view({'post': 'create', 'get': 'list'})
retrieveUpdate = views.ConversationMessagingViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'})
urlpatterns = [
    path('conversations/', listCreate, name='conversation-list'),
    path('conversations/<uuid:pk>', retrieveUpdate, name='conversation-detail')
]
