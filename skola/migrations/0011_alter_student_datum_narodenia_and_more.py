# Generated by Django 4.2.7 on 2024-04-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0010_alter_student_datum_narodenia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='datum_narodenia',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ucitel',
            name='datum_narodenia',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
