from django.urls import path
from . import views

# app_name = covid_blog    # What is the need of this? its giving an error
urlpatterns = [
	path('', views.index, name='index'),
	path('details/<int:article_id>', views.details, name='details'),
	path('submit-article', views.submit_article, name='submit_article'),

	path('article-djangoform', views.article_djangoform, name='article_djangoform')
	]