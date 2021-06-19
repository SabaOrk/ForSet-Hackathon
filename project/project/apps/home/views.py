from django.shortcuts import render
from .models import Topic

# Create your views here.
def home(request):

	topics = Topic.objects.all()

	context = {
		'topics':topics
	}

	return render(request, 'home.html', context)


def topic(request, slug):

	title = slug.replace('_',' ')

	topic = Topic.objects.get(title=title)

	context = {
		'topic':topic
	}

	return render(request, 'topic.html', context)

def about(request):

	context = {

	}

	return render(request, 'about.html', context)

