from django.shortcuts import render
from project.apps.home.models import Category, SubCategory
# Create your views here.
def sub_categories(request, category):

	category = Category.objects.get(name=category)
	sub_categories = SubCategory.objects.filter(category=category)

	context = {
		'category':category,
		'sub_categories':sub_categories
	}

	return render(request, 'subcategory.html', context)