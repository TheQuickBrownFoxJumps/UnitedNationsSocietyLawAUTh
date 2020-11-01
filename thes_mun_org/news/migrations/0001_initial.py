# Generated by Django 3.0.6 on 2020-10-21 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('author', models.TextField(verbose_name='Author')),
                ('publication_date', models.DateTimeField(verbose_name='Date Published')),
                ('hero_image', models.TextField(verbose_name='Hero Image')),
                ('additional_image', models.TextField(blank=True, null=True, verbose_name='Additonal Image')),
                ('body_text', models.TextField(verbose_name='Body')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category')),
            ],
        ),
    ]
