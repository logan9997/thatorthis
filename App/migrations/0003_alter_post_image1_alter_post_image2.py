# Generated by Django 4.2.2 on 2023-06-12 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_post_title_alter_post_image1_alter_post_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
