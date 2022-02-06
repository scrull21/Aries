from unicodedata import category
from django.shortcuts import render
from apps.news.models import News, Tags
from django.db.models import F
from apps.categories.models import Category

# Create your views here.

def news_detail(request, id):
    news = News.objects.get(id=id)
    category = Category.objects.all().order_by('-id')[:5]
    tags = Tags.objects.all()
    related_news = News.objects.all().order_by('-created', )[:2]
    context = {
        'news' : news,
        'categories' : category,
        'tags' : tags,
        'related_news' : related_news
    }
    return render(request, 'news/detail.html', context)