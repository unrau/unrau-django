import datetime

from django.db import models
from django.utils import timezone

STATUS = (
    (0,"Draft"),
    (1,"Published")
)

class KnotEntry(models.Model):
    title_text = models.CharField(max_length=200)
    page_num = models.IntegerField(default=0, unique=True)
    comic_image = models.ImageField(upload_to='kotw')
    content_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-page_num', 'pk']

    def __str__(self):
        return self.title_text

    def _prev_page(self):
        prevpage = self.page_num - 1
        if prevpage >= 0:
            return prevpage
        else:
            return 0
    previous = property(_prev_page)

    def _next_page(self):
        latestpage = KnotEntry.objects.latest('page_num')
        nextpage = self.page_num + 1
        if nextpage < latestpage.page_num:
            return nextpage
        else:
            return latestpage.page_num
    next = property(_next_page)

    def _latest_page(self):
        return KnotEntry.objects.latest('page_num').page_num
    latest = property(_latest_page)