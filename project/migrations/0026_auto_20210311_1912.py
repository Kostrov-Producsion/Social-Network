# Generated by Django 2.2.6 on 2021-03-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0025_auto_20210311_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='descriptionAlbum',
            field=models.CharField(max_length=150),
        ),
    ]
