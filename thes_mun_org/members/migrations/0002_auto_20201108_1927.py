# Generated by Django 3.0.6 on 2020-11-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmember',
            name='member_pic',
            field=models.ImageField(blank=True, default='test.png', null=True, upload_to='members/members_pic'),
        ),
        migrations.AlterField(
            model_name='boardmember',
            name='role',
            field=models.CharField(choices=[('P', 'President'), ('VP', 'Vice-President'), ('SG', 'Secretary-General'), ('TR', 'Treasurer'), ('AL', 'Director for Communications and Merketing')], max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='historicalboardmember',
            name='member_pic',
            field=models.TextField(blank=True, default='test.png', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalboardmember',
            name='role',
            field=models.CharField(choices=[('P', 'President'), ('VP', 'Vice-President'), ('SG', 'Secretary-General'), ('TR', 'Treasurer'), ('AL', 'Director for Communications and Merketing')], db_index=True, max_length=2),
        ),
    ]