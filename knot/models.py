import datetime

from django.db import models
from django.utils import timezone

STATUS = (
    (0,"Draft"),
    (1,"Published")
)

class KnotEntry(models.Model):
    title_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    page_num = models.IntegerField(default=0)
    comic_image = models.ImageField(upload_to='kotw')
    content_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-pub_date', 'pk']

    def __str__(self):
        return self.title_text
