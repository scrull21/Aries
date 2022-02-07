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
    navbar_news = News.objects.all().order_by('-created',)[:5]
    categories_navbar = Category.objects.all().order_by('-created',)[:5]
    popular_news = News.objects.all().order_by('news_comment', )[:10]
    context = {
        'news' : news,
        'settings' : set,
        'top_news' : top_news,
        'news_slide' : news_slide,
        'random_news' : random_news,
        'navbar_news' : navbar_news,
        'categories_navbar' : categories_navbar,
        'popular_news' : popular_news
    }
    return render(request, 'news/index.html', context)

def about_us(request):
    return render(request, 'about.html')
