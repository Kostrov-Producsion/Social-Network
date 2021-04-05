# Generated by Django 2.2.6 on 2021-03-23 10:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0031_group_quote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_pub']},
        ),
        migrations.AddField(
            model_name='audio',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='last_online',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]