# Generated by Django 3.1.5 on 2021-04-11 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_notification_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='type',
            new_name='notification_type',
        ),
    ]