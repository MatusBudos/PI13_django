# Generated by Django 4.2.7 on 2023-12-15 10:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='datum',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
