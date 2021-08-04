# Generated by Django 3.2.5 on 2021-07-23 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_name', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=500)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('location', models.CharField(max_length=30)),
                ('event_title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_type', models.CharField(max_length=50)),
                ('total_likes', models.CharField(max_length=10)),
                ('comments', models.TextField(max_length=200)),
                ('content', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('members', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('category', models.CharField(max_length=30)),
                ('website_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField(max_length=500)),
                ('birth_date', models.DateField()),
                ('fav_movies', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('photo_url', models.URLField()),
            ],
        ),
    ]