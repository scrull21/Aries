from django.shortcuts import render
from apps.news.models import News

# Create your views here.
def index(request):
    news = News.objects.all()
    context = {
        'news' : news 
    }
    return render(request, 'news/index.html', context)