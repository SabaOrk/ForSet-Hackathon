from django.shortcuts import render
from .models import Topic, Experience, SubCategory, Category
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse


# Create your views here.
def home(request):


	context = {
		
	}

	return render(request, 'index2.html', context)


def topic(request, topic):

	topic = Topic.objects.get(pk=topic)

	context = {
		'topic':topic,
		'bg':topic.main_category.bg
	}

	return render(request, 'topic.html', context)


def add_experience(request, topic):

	try:
		topic = Topic.objects.get(pk=topic)

		if request.method == 'POST':
			email = request.POST.get('email')
			text = request.POST.get('text')

			experience = Experience.objects.create(email=email, text=text)

			return JsonResponse({'result': True}, status=200)

	except Exception as ex:

		print(ex)
		return JsonResponse({'result': 'Failed'}, status=200)

def sub_categories(request, pk):

	category = Category.objects.get(pk=pk)
	print(category.name)
	sub_categories = SubCategory.objects.filter(category=category)
	topics = Topic.objects.filter(main_category=category)
	print(topics)

	context = {
		'category':category,
		'sub_categories':sub_categories,
		'topics': topics
	}

	return render(request, 'subcategory.html', context)



def relate_to_topic(request, topic):

	topic = Topic.objects.get(pk=topic)

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


def check_related(request, topic):
	try:
		topic = Topic.objects.get(pk=topic)

		return JsonResponse({'result': request.session['related']}, status=200)

	except Exception as ex:
		print(ex)

		return JsonResponse({'result': 'Empty'}, status=200)


def about(request):

	context = {

	}

	return render(request, 'about.html', context)

