# Generated by Django 4.1.7 on 2023-06-11 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('description1', models.CharField(max_length=500)),
                ('description2', models.CharField(max_length=500)),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], max_length=6)),
                ('date_posted', models.DateField()),
                ('tags', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=60)),
                ('password', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('vote_id', models.AutoField(primary_key=True, serialize=False)),
                ('option', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=1)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user'),
        ),
    ]
