# Generated by Django 2.2.3 on 2020-03-23 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pawbook', '0009_auto_20200308_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]