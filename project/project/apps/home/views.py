from django.shortcuts import render
from .models import Topic

# Create your views here.
def home(request):

	windows = Window.objects.all()

	context = {
		'windows':windows
	}

	return render(request, 'home.html', context)


def topic(request, title):

	topic = Topic.objects.get(title=title)

	context = {
		'topic':topic
	}

	return render(request, 'topic.html', context)

def about(request):

	context = {

	}

	return render(request, 'about.html', context)

