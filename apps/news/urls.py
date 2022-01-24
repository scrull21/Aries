from django.urls import path 
from apps.news.views import index, news_detail


urlpatterns = [
    path('', index, name = 'index'),
    path('news/<int:id>/', news_detail, name = "news_detail")
]