from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	
	def __str__(self):
		return self.name

class Topic(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	main_category = models.OneToOneField(Category, default=None, on_delete=models.CASCADE, related_name='main_category')
	sub_category = models.OneToOneField(Category, default=None, on_delete=models.CASCADE, related_name='sub_category')
	relation_count = models.IntegerField(default=0)

	def __str__(self):
		return self.title
class Experience(models.Model):
	email = models.EmailField(max_length=255, blank=False, null=False)
	text = models.TextField()
	date_created = models.DateTimeField(auto_now=True)
	approved = models.BooleanField(default=False)