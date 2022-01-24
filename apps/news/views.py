from django.shortcuts import render
from apps.news.models import News
from django.db.models import F

# Create your views here.
def index(request):
    news = News.objects.all()
    context = {
        'news' : news 
    }
    return render(request, 'news/index.html', context)

def news_detail(request, id):
    news = News.objects.get(id=id)
    context = {
        'news' : news,
    }
    return render(request, 'news/detail.html', context)