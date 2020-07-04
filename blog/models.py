import datetime

from django.db import models
from django.utils import timezone

class BlogEntry(models.Model):
    title_text = models.CharField(max_length=200)
    content_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title_text
