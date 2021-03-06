from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	bg = models.CharField(max_length=30)
	
	def __str__(self):
		return self.name

class SubCategory(models.Model):
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Topic(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	svg = models.CharField(max_length=200, blank=True, null=True)
	main_category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE, related_name='main_category')
	sub_category = models.ForeignKey(SubCategory, default=None, on_delete=models.CASCADE, related_name='sub_category')
	relation_count = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Experience(models.Model):
	email = models.EmailField(max_length=255, blank=False, null=False)
	topic = models.ForeignKey(Topic, default=None, on_delete=models.CASCADE, related_name='topic')
	text = models.TextField()
	date_created = models.DateTimeField(auto_now=True)
	approved = models.BooleanField(default=False)

	def __str__(self):
		return self.email


