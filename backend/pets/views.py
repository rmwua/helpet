from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from pets.models import Appointment, Pet, MedicalHistoryItem, Note
from pets.serializers import (AppointmentSerializer, PetSerializer, MedicalHistoryItemSerializer, UserSerializer,
                              NoteSerializer)


class GenericAppointmentView(generics.GenericAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(pet__user=user)


class AppointmentListView(GenericAppointmentView, generics.ListCreateAPIView):
    pass


class AppointmentDetailView(GenericAppointmentView, generics.RetrieveUpdateDestroyAPIView):
    pass


class GenericPetView(generics.GenericAPIView):
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Pet.objects.filter(user=user)


class PetListView(GenericPetView, generics.ListCreateAPIView):
    parser_classes = [MultiPartParser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PetDetailView(GenericPetView, generics.RetrieveUpdateDestroyAPIView):
    pass


class GenericMedicalHistoryItemView(generics.GenericAPIView):
    serializer_class = MedicalHistoryItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return MedicalHistoryItem.objects.filter(pet__user=user)


class MedicalHistoryItemListView(GenericMedicalHistoryItemView, generics.ListCreateAPIView):
    pass


class MedicalHistoryItemDetailView(GenericMedicalHistoryItemView, generics.RetrieveUpdateDestroyAPIView):
    pass


class GenericNoteView(generics.GenericAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)


class NoteListView(GenericNoteView, generics.ListCreateAPIView):

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteDetailView(GenericNoteView, generics.RetrieveUpdateDestroyAPIView):
    pass


class GenericUserView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)


class UserListView(GenericUserView, generics.ListAPIView):
    pass


class UserDetailView(GenericUserView, generics.RetrieveAPIView):
    pass
