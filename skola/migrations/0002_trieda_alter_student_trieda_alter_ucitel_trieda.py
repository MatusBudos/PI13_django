# Generated by Django 4.2.7 on 2023-12-01 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trieda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='trieda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skola.trieda'),
        ),
        migrations.AlterField(
            model_name='ucitel',
            name='trieda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skola.trieda'),
        ),
    ]
