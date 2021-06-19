from django.shortcuts import render
from .models import Window

# Create your views here.
def home(request):

	windows = Window.objects.all()

	context = {
		'windows':windows
	}

	return render(request, 'home.html', context)
