from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=100)
	details = models.TextField()
	pub_date = models.DateTimeField('date published')
