# Generated by Django 5.0.2 on 2024-05-02 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCredential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('expenses', models.IntegerField(blank=True, null=True)),
                ('area', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Tracker.customercredential')),
            ],
        ),
    ]
