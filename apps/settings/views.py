from django.conf import Settings
from django.shortcuts import render
from apps.settings.models import Setting
from apps.news.models import News, NewsLike

# Create your views here.
def index(request):
    news = News.objects.all()
    news_slide = News.objects.all().order_by('-created',)[:3]
    set = Setting.objects.get(pk=1)
    top_news = NewsLike.objects.all().order_by('-news_liked',)[:6]
    context = {
        'news' : news,
        'settings' : set,
        'top_news' : top_news,
        'news_slide' : news_slide,
    }
    return render(request, 'news/index.html', context)