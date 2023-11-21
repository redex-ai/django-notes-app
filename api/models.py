{
  "codeChangeList": [
    {
      "filePath": "api/models.py",
      "code": "```\nfrom django.db import models\n\n# Create your models here.\n\nclass Note(models.Model):\n    body = models.TextField(null=True, blank=True)\n    updated = models.DateTimeField(auto_now=True)\n    created = models.DateTimeField(auto_now_add=True)\n\n    def __str__(self):\n        return self.body[0:50] + '...' if len(self.body) > 50 else self.body\n```\n"
    }
  ]
}
