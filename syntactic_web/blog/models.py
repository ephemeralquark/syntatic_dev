from django.db import models
import datetime

# Create your models here.
class Article(models.Model):
    heading = models.CharField(max_length=200)
    byline = models.CharField(max_length=200, null=True)
    publish_date = models.DateField('date published', default=datetime.date)
    active = models.BinaryField()
    text = models.CharField(max_length=200)
