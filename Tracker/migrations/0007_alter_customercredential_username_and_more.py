# Generated by Django 5.0.2 on 2024-05-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0006_alter_customerdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercredential',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='user',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
