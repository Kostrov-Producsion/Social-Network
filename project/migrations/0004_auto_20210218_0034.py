# Generated by Django 2.2.6 on 2021-02-17 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210215_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_update',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modified',
            field=models.DateTimeField(blank=True),
        ),
    ]