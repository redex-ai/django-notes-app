{
  "codeChangeList": [
    {
      "filePath": "api/management/commands/backup_notes.py",
      "code": "from django.core.management.base import BaseCommand, CommandError\nfrom api.models import Note\nimport json\nimport os\nfrom datetime import datetime\n\n\nclass Command(BaseCommand):\n    help = 'Back up all notes to a JSON file'\n\n    def add_arguments(self, parser):\n        parser.add_argument('backup_dir', type=str, help='Directory where the backup file will be saved')\n\n    def handle(self, *args, **options):\n        backup_dir = options['backup_dir']\n        if not os.path.isdir(backup_dir):\n            raise CommandError('Backup directory does not exist')\n\n        notes = list(Note.objects.all().values())\n        filename = f'notes_backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.json'\n        file_path = os.path.join(backup_dir, filename)\n\n        with open(file_path, 'w') as outfile:\n            json.dump(notes, outfile)\n\n        self.stdout.write(self.style.SUCCESS(f'Successfully backed up notes to {file_path}'))\n"
    },
    {
      "filePath": "api/management/__init__.py",
      "code": ""
    }
  ]
}
