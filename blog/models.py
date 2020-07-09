import datetime

from django.db import models
from django.utils import timezone

STATUS = (
    (0,"Draft"),
    (1,"Published")
)

class BlogEntry(models.Model):
    title_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-pub_date']

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title_text
