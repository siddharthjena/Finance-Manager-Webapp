# Generated by Django 5.0.2 on 2024-05-02 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercredential',
            name='total_exp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customercredential',
            name='total_inc',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]