# Generated by Django 5.0.7 on 2024-07-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='location',
            field=models.CharField(default='Nairobi', max_length=20),
        ),
    ]