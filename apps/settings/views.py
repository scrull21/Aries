from django.conf import Settings
from django.shortcuts import render
from apps.settings.models import Setting
from apps.news.models import News, NewsLike
from apps.categories.models import Category

# Create your views here.
def index(request):
    news = News.objects.all()
    news_slide = News.objects.all().order_by('-created',)[:5]
    set = Setting.objects.get(pk=1)
    top_news = NewsLike.objects.all().order_by('-news_liked',)[:6]
    random_news = News.objects.order_by('?').first()
    context = {
        'news' : news,
        'settings' : set,
        'top_news' : top_news,
        'news_slide' : news_slide,
        'random_news' : random_news,
    }
    return render(request, 'news/index.html', context)

def navbar(request):
    category = Category.objects.all().order_by('-id')[:5]
    context = {
        'categories' : category
    }
    return render(request, 'include/navbar.html', context)