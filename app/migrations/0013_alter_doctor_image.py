# Generated by Django 5.0.4 on 2024-05-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_patient_image_alter_patient_mobileno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(upload_to='Doctore'),
        ),
    ]
