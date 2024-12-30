from django.urls import path
from . views import OsnovView, NewsDetailView, NewsListView, AddComment
from . views import contact_view, love, new_year



urlpatterns = [
    path('news/', NewsListView.as_view(), name='news_list'),
	path('news-post/<slug:slug>/', NewsDetailView.as_view(), name='news-list'),
	path('', OsnovView.as_view(), name='index'),
	path('contact/', contact_view, name='contact'),
	path('comment/', AddComment.as_view(), name='comment'),
	#animations
	path('love/', love, name='love'),
	path('new-year', new_year, name='new-year')
]