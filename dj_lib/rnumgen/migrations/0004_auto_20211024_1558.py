# Generated by Django 3.2.7 on 2021-10-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rnumgen', '0003_remove_employee_rcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='fname',
            field=models.CharField(default='', max_length=80, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='employee',
            name='lname',
            field=models.CharField(default='', max_length=80, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='employee',
            name='rcode',
            field=models.CharField(db_index=True, default='', max_length=5, unique=True, verbose_name='Employee Report code'),
        ),
        migrations.AddField(
            model_name='report',
            name='name',
            field=models.CharField(default='', max_length=120, verbose_name='Client Name'),
        ),
        migrations.AddField(
            model_name='report',
            name='rnumber',
            field=models.PositiveIntegerField(db_index=True, null=True, unique=True, verbose_name='Report Number'),
        ),
        migrations.AddField(
            model_name='report',
            name='rtype',
            field=models.CharField(choices=[('A', 'ASC'), ('B', 'BASC')], default='', max_length=1, verbose_name='Type of Report'),
        ),
    ]
