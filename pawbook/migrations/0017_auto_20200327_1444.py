# Generated by Django 2.2.3 on 2020-03-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawbook', '0016_auto_20200327_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='petImage',
            field=models.ImageField(storage='/home/p/Desktop/Filez/ScHool/UniGlasgow/YearTwo/Semester 2/Web Apps/Group/pawbook_wad/media/listing_image/', upload_to='listing_image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.ImageField(storage='/home/p/Desktop/Filez/ScHool/UniGlasgow/YearTwo/Semester 2/Web Apps/Group/pawbook_wad/media/post_image/', upload_to='post_image'),
        ),
    ]