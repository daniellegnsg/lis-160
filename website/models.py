from django.db import models


class Book(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)
	year_published = models.CharField(max_length=4)

	def __str__(self):
		return(f"{self.title}")