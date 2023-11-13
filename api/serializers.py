from rest_framework import serializers  # Import serializers
from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Note
        fields = '__all__'