from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Article(models.Model):
    heading = models.CharField(max_length=200)
    byline = models.CharField(max_length=200, null=True)
    publish_date = models.DateField('date published', default=timezone.now)
    active = models.BinaryField()
    text = models.CharField(max_length=200)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publish_date <= now
