from django.urls import path

from pets import views

urlpatterns = [
    path('appointments/', views.AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('pets/', views.PetListView.as_view(), name='pet-list'),
    path('pets/<int:pk>/', views.PetDetailView.as_view(), name='pet-detail'),
    path('medical-history-items/', views.MedicalHistoryItemListView.as_view(), name='medical-history-item-list'),
    path('medical-history-items/<int:pk>/',
         views.MedicalHistoryItemDetailView.as_view(),
         name='medical-history-item-detail'),
    path('notes/', views.NoteListView.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetailView.as_view(), name='note-detail'),
    path('users/',
         views.UserListView.as_view(),
         name='user-list'),
    path('users/<int:pk>/',
         views.UserDetailView.as_view(),
         name='user-detail')
]
