# Generated by Django 5.0.1 on 2024-03-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priklad',
            name='vysledok',
            field=models.FloatField(max_length=2),
        ),
    ]
