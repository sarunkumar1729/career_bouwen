# Generated by Django 5.0.2 on 2024-02-22 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CB_app', '0005_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='short_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='job',
            name='long_description',
        ),
    ]
