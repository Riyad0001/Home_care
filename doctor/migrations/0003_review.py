# Generated by Django 5.1.4 on 2025-01-08 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_remove_doctor_availabletime_doctor_availabletime'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(choices=[('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐', '⭐⭐'), ('⭐', '⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐')], max_length=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
