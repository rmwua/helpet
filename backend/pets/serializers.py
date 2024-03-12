from django.contrib.auth.models import User
from rest_framework import serializers

from pets.models import Appointment, MedicalHistoryItem, Pet, Note


class PetSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pet-detail')
    appointments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="appointment-detail")
    medical_history_items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="medical-history-item-detail")
    notes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="note-detail"
    )
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Pet
        fields = ['url',
                  'name',
                  'species',
                  'breed',
                  'microchip',
                  'avatar',
                  'special_needs',
                  'user',
                  'appointments',
                  'medical_history_items',
                  'notes']


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='appointment-detail')

    class Meta:
        model = Appointment
        fields = ['url', 'name', 'type', 'date', 'note', 'pet', ]

    def get_fields(self):
        fields = super().get_fields()
        user = self.context['request'].user
        fields['pet'] = serializers.HyperlinkedRelatedField(view_name="pet-detail",
                                                            queryset=Pet.objects.filter(user=user))
        return fields


class MedicalHistoryItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='medical-history-item-detail')

    def get_fields(self):
        fields = super().get_fields()
        user = self.context['request'].user
        fields['pet'] = serializers.HyperlinkedRelatedField(view_name="pet-detail",
                                                            queryset=Pet.objects.filter(user=user))
        return fields

    class Meta:
        model = MedicalHistoryItem
        fields = ['url', 'name', 'type', 'date', 'note', 'pet', ]


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='note-detail')
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Note
        fields = ['url', 'title', 'body', 'user']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = User
        fields = ['url', 'username', 'pet_set', 'note_set']
