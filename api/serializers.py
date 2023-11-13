import logging
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Note

logger = logging.getLogger(__name__)

class NoteSerializer(ModelSerializer):
    updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Note
        fields = '__all__'

    def to_representation(self, instance):
        logger.info(f"Serializing Note object with id {instance.id}")
        return super().to_representation(instance)

    def to_internal_value(self, data):
        logger.info("Deserializing Note object")
        return super().to_internal_value(data)
