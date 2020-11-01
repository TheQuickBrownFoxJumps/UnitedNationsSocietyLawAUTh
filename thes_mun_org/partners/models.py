from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


# Create your models here.

class Partner(models.Model):
    position = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    image = ProcessedImageField(upload_to='partners', processors=[ResizeToFit(300)], format='JPEG',
                                options={'quality': 90}, default='test.png')
    content = models.TextField(max_length=500)


class Supporter(models.Model):
    name = models.CharField(max_length=100)
    image = ProcessedImageField(upload_to='partners', processors=[ResizeToFit(300)], format='JPEG',
                                options={'quality': 90}, default='test.png')
    content = models.TextField(max_length=500)
