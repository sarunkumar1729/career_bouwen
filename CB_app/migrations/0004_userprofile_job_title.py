# Generated by Django 5.0.2 on 2024-02-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_app', '0003_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='job_title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
