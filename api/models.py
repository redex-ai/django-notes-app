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
        logger.info(f"Saving note: {self.body}")
        super().save(*args, **kwargs)
        logger.info(f"Note saved: {self.body}")

    def delete(self, *args, **kwargs):
        logger.info(f"Deleting note: {self.body}")
        super().delete(*args, **kwargs)
        logger.info(f"Note deleted: {self.body}")
