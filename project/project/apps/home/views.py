from django.shortcuts import render
from .models import Topic
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse


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

def relate_to_topic(request, title):

	topic = Topic.objects.get(title=title)

	if request.session.get('related') == False:
		topic.relation_count += 1
		topic.save()

		request.session['related'] = True

		return JsonResponse({'result': True, 'count':topic.relation_count}, status=200)
	else:
		topic.relation_count -= 1
		topic.save()

		request.session['related'] = False

		return JsonResponse({'result': False, 'count':topic.relation_count}, status=200)


def check_related(request, title):

	topic = Topic.objects.get(title=title)

	return JsonResponse({'result': request.session['related']}, status=200)


def about(request):

	context = {

	}

	return render(request, 'about.html', context)

