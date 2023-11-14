from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Note
        fields = ['title', 'body', 'updated', 'created']
