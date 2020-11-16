# Generated by Django 3.0.6 on 2020-11-16 15:42

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20201116_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default='test.png', help_text='Presentation Image', upload_to='news'),
        ),
        migrations.AlterField(
            model_name='new',
            name='image_detail',
            field=imagekit.models.fields.ProcessedImageField(default='test.png', help_text='Second Image for Detail view', upload_to='news'),
        ),
    ]
