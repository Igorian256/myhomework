from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News

class NewsListView(ListView):
    model = News
    queryset = News.objects.order_by('-date')
    template_name = 'news_list.html'
    context_object_name = 'news_list'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'
