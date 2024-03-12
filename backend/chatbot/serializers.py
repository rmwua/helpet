from rest_framework import serializers
from chatbot.models import Conversation


class ConversationMessageSerializer(serializers.Serializer):
    message = serializers.CharField()


class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="conversation-detail")
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Conversation
        fields = ['url', 'messages', 'user']
