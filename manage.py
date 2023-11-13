#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging

logger = logging.getLogger(__name__)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notesapp.settings')
    try:
        from django.core.management import execute_from_command_line
        logger.info("Executing command: {}".format(' '.join(sys.argv)))
        execute_from_command_line(sys.argv)
        logger.info("Command execution completed.")
    except ImportError as exc:
        logger.error("Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?")
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    except Exception as e:
        logger.error("An error occurred while executing the command: {}".format(e))
        raise e


if __name__ == '__main__':
    main()
