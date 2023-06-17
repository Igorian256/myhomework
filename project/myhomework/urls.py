from django.urls import path
from news.views import NewsListView, NewsDetailView

app_name = 'news'

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]
