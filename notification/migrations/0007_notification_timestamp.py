# Generated by Django 2.2.15 on 2020-08-25 19:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_notification_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 8, 25, 19, 48, 12, 556232, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
