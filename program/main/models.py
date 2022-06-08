from django.db import models
from django.urls import reverse


class Tag(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)

	def __str__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)

	def __str__(self):
		return self.name 


class Book(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	author = models.ManyToManyField(Author, related_name='authors')
	body = models.TextField()
	image = models.ImageField(upload_to='images')
	created = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag, related_name='tags')

	class Meta:
		ordering = ('-created', )

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', args=[self.slug])


class Comment(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)