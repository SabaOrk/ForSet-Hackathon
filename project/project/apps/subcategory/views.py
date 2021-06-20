from django.shortcuts import render
from project.apps.home import models as home_models
# Create your views here.
def sub_categories(request, category):

	category = home_models.Category.objects.get(name=category)
	sub_categories = home_models.SubCategory.objects.filter(category=category)

	context = {
		'category':category,
		'sub_categories':sub_categories
	}

	return render(request, 'home.html', context)