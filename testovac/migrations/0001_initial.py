# Generated by Django 5.0.1 on 2024-02-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priklad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField()),
                ('b', models.FloatField()),
                ('operator', models.CharField(max_length=1)),
                ('vysledok', models.FloatField()),
            ],
        ),
    ]