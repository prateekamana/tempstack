from .views import ArticlesListView, ArticlesDetailedView
from django.urls import path


urlpatterns = [

	path('', ArticlesListView.as_view()),
	path('<pk>', ArticlesDetailedView.as_view()),
	
]