from django.shortcuts import render
from apps.categories.models import Category
from apps.news.models import News

# Create your views here.
def category_index(request):
    category = Category.objects.all()
    news = News.objects.all().order_by('-created',)[:10]
    context = {
        'categories' : category,
        'news' : news,
    }
    return render(request, 'categories/index.html', context)

def category_detail(request, slug):
    news = News.objects.get(slug = slug)
    context = { 
        'category' : news,
    }
    return render(request, 'categories/detail.html', context)