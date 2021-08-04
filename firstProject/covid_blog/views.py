from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import Article
from .forms import ArticleForm


# Create your views here.

def index(request):
	'''
	STEPS: 
		1. Fetch the data according to request from DB
		2. Create a context that can be sent to a particular template
		3. Receive the context in template & Write DTL code
	'''
	context = {
		'all_articles' : Article.objects.all()
	}

# OPTION_1 : to render template
	response_template = loader.get_template('covid_blog/index.html')
	return HttpResponse(response_template.render(context, request))

# OPTION_2:
#	return render(request, 'covid_blog/index.html', context)

def details(request, article_id):
	result = Article.objects.get(pk=article_id)
	context = {
		'article' : result
	}

	return render(request, 'covid_blog/details.html', context)

def submit_article(request):
	if request.method == 'GET':
		return render(request, 'covid_blog/submit_article.html', {})

	elif request.method == 'POST':
		article = Article(title=request.POST['title'], details=request.POST['details'], pub_date=timezone.now())
		article.save()

		context = {
			'all_articles' : Article.objects.all()
		}
		return render(request, 'covid_blog/index.html', context)
		
		# return index(request) # NOT A GOOD IDEA TO CALL ANOTHER FUNCTION
		# return HttpResponse('New Article Saved Successfully')

	else:
		print('Something wrong tarun')
		return render(request, 'covid_blog/submit_article.html', {})

# Django-Forms:

def article_djangoform(request):
	if request.method == 'POST':
		# Extract data from request:
		a_form = ArticleForm(request.POST)

		# Save the data:
		if a_form.is_valid():
			a_form.save()
			return HttpResponse("Successfully Saved :-)")
		else:
			return HttpResponse("Error in saving the Article")
	else:
		context = {
			'djangoform'  : ArticleForm()
		}
		return render(request, 'covid_blog/article_djangoform.html', context)

''' 
Django is using templates (template files, e.g. html templates). The render shortcut 
will take a template name as an argument, and then render this template with the 
given parameters and then return an HttpResponse with the rendered body. HttpResponse
instead does just what the name indicates, dealing with HTTP responses. It does not
do the stuff Django does behind the scenes when calling render and in case you want 
to return a rendered Django template you would need to do this manually and pass 
that result to the HttpResponse before returning. – Torsten Engelbrecht 
'''