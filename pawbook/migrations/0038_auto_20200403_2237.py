# Generated by Django 2.2.3 on 2020-04-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawbook', '0037_merge_20200403_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
