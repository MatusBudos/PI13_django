# Generated by Django 4.2.7 on 2024-04-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0008_alter_ucitel_datum_narodenia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='datum_narodenia',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
