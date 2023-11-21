import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from api.models import Note

class Command(BaseCommand):
    help = 'Back up all notes to a JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--backup-dir',
            type=str,
            help='Directory where the backup file will be saved',
            default=os.path.join(settings.BASE_DIR, 'backups')
        )

    def handle(self, *args, **options):
        backup_dir = options['backup_dir']
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        backup_file_path = os.path.join(backup_dir, 'notes_backup.json')
        notes = list(Note.objects.all().values())
        with open(backup_file_path, 'w') as backup_file:
            json.dump(notes, backup_file)

        self.stdout.write(self.style.SUCCESS(f'Successfully backed up notes to {backup_file_path}'))
