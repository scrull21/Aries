from django.shortcuts import render
from apps.categories.models import Category

# Create your views here.
def category_index(request):
    category = Category.objects.all()
    context = {
        'categories' : category,
    }
    return render(request, 'categories/index.html', context)