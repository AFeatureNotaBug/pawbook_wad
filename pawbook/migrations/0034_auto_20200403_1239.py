# Generated by Django 2.2.3 on 2020-04-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawbook', '0033_auto_20200403_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='petImage',
            field=models.ImageField(upload_to='listing_image/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.ImageField(upload_to='post_image/'),
        ),
    ]