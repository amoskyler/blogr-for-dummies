from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	"""represents a blog post"""
	author = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	text = models.TextField()
	pub_date = models.DateTimeField('date published')

class Comment(models.Model):
	"""represents a comment on a blog post"""
	post = models.ForeignKey('Post')
	author = models.ForeignKey(User)
	text = models.CharField(max_length=140)
	pub_date = models.DateTimeField('date published')