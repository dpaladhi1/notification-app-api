# Generated by Django 3.2.25 on 2025-07-24 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_notification_createtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='createtime',
            field=models.TimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
