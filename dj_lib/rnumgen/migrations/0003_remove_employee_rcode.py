# Generated by Django 3.2.7 on 2021-10-24 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnumgen', '0002_auto_20211024_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='rcode',
        ),
    ]
