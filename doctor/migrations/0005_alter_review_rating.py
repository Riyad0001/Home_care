# Generated by Django 5.1.4 on 2025-01-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐', '⭐'), ('⭐⭐⭐', '⭐⭐⭐')], max_length=10),
        ),
    ]
