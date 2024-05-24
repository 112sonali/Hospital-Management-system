# Generated by Django 5.0.4 on 2024-05-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('mobileno', models.IntegerField()),
                ('doctor', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('dob', models.DateField()),
                ('report', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='profile')),
            ],
        ),
    ]
