# Generated by Django 3.0.5 on 2020-04-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppe', '0013_auto_20200412_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilitydelivery',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
