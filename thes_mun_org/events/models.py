from django.db import models
from datetime import datetime
# import the user model
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = ProcessedImageField(upload_to='events', processors=[ResizeToFit(300)], format='JPEG',
                                options={'quality': 90}, default='test.png')
    date = models.DateField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, default='slug-like-that')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'pk': self.pk})
