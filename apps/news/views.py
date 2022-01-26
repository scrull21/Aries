from django.shortcuts import render
from apps.news.models import News
from django.db.models import F

# Create your views here.
def navbar_news(request):
    navbar = News.objects.all().order_by('-created',)[:5]
    context = {
        'navbar' : navbar
    }
    return render(request, 'include/navbar.html', context)


def news_detail(request, id):
    news = News.objects.get(id=id)
    context = {
        'news' : news,
    }
    return render(request, 'news/detail.html', context)