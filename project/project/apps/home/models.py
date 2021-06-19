from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	

class Topic(models.Model):
	title = models.CharField(max_length=255)
	main_category = models.OneToOneField(Category, default=None, on_delete=models.CASCADE, related_name='main_category')
	sub_category = models.OneToOneField(Category, default=None, on_delete=models.CASCADE, related_name='sub_category')
	count = models.IntegerField(default=0)
