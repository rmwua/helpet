import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    messages = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
