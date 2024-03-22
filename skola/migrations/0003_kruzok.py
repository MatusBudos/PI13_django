# Generated by Django 4.2.7 on 2024-03-22 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0002_trieda_alter_student_trieda_alter_ucitel_trieda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kruzok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=100)),
                ('skratka', models.CharField(max_length=3)),
                ('ucitel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skola.ucitel')),
            ],
        ),
    ]
