# Generated by Django 5.1.4 on 2025-01-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='availableTime',
        ),
        migrations.AddField(
            model_name='doctor',
            name='availableTime',
            field=models.ManyToManyField(to='doctor.availabletime'),
        ),
    ]
