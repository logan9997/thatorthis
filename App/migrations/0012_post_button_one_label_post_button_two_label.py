# Generated by Django 4.2.2 on 2023-06-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_rename_vote_postvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='button_one_label',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='button_two_label',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]