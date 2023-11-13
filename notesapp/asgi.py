"""
ASGI config for notesapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import logging

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notesapp.settings')

logger = logging.getLogger(__name__)

try:
    application = get_asgi_application()
    logger.info("ASGI server started successfully.")
except Exception as e:
    logger.exception("Failed to start ASGI server: %s", str(e))
    raise
