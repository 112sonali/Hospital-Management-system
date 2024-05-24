# Generated by Django 5.0.4 on 2024-05-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_doctor_delete_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('experience', models.CharField(max_length=200)),
                ('specialization', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('mobileno', models.IntegerField()),
                ('password', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='profile')),
            ],
        ),
    ]
