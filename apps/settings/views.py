from django.conf import Settings
from django.shortcuts import render
from apps.settings.models import Setting
from apps.news.models import News

# Create your views here.
def index(request):
    news = News.objects.all()
    set = Setting.objects.get(pk=1)
    context = {
        'news' : news,
        'settings' : set,
    }
    return render(request, 'news/index.html', context)