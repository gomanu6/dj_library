# Generated by Django 3.2.7 on 2021-10-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_lib', '0002_book_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_slug',
            field=models.SlugField(default=''),
        ),
    ]
