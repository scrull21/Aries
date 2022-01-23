from django.urls import path 
from apps.news.views import index


urlpatterns = [
    path('', index, name = 'index'),
]