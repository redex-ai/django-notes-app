import logging
from django.db import models

logger = logging.getLogger(__name__)

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:69]

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            logger.info("Note saved successfully")
        except Exception as e:
            logger.error(f"Error saving note: {str(e)}")

    def delete(self, *args, **kwargs):
        try:
            super().delete(*args, **kwargs)
            logger.info("Note deleted successfully")
        except Exception as e:
            logger.error(f"Error deleting note: {str(e)}")
