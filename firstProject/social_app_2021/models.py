from django.db import models

# Create your models here.

class UserProfile(models.Model):
	# UserProfile(about_me='', birth_date='', fav_movies='', first_name='', last_name='', username='', photo_url='')
	about_me = models.TextField(max_length=500)
	birth_date = models.DateField()
	fav_movies = models.CharField(max_length=100)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	username = models.CharField(max_length=20)
	photo_url = models.URLField()

class Group(models.Model):
	# Group(name='', members='', description='', category='', website_url='')
	name = models.CharField(max_length=50)
	members = models.TextField(max_length=100)
	description = models.TextField(max_length=500)
	category = models.CharField(max_length=30)
	website_url = models.URLField()

class Event(models.Model):
	creator_name = models.CharField(max_length=40)
	description = models.TextField(max_length=500)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	location = models.CharField(max_length=30)
	event_title = models.CharField(max_length=30)

class Feed(models.Model):
	feed_type = models.CharField(max_length=50)
	total_likes = models.CharField(max_length=10)
	comments = models.TextField(max_length=200)
	content = models.TextField(max_length=300)

