# Generated by Django 3.0.6 on 2020-11-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20201116_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='href_url',
            field=models.URLField(default='', help_text='Add here any site reference.'),
        ),
    ]
