# Generated by Django 5.0.4 on 2024-05-25 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='mobileno',
            field=models.BigIntegerField(),
        ),
    ]
