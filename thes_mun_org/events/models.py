from django.db import models
from datetime import datetime
# import the user model
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.conf import settings
from django.utils.text import slugify


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = ProcessedImageField(upload_to='events', processors=[ResizeToFit(300)], format='JPEG',
                                options={'quality': 90}, default='test.png',
                                help_text='Presentation Image')
    image_detail = ProcessedImageField(upload_to='events', processors=[ResizeToFit(300)], format='JPEG',
                                       options={'quality': 90}, default='test.png',
                                       help_text='Second Image for Detail view')
    date = models.DateField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(default='', editable=False, max_length=100)
    href_url = models.URLField(default='', null=True, blank=True, help_text='Add here any site reference.')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_post_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
