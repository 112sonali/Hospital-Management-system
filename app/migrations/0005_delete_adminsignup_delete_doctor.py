# Generated by Django 5.0.4 on 2024-05-21 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_patient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdminSignup',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
