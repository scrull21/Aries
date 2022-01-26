from django.urls import path 
from apps.news.views import news_detail


urlpatterns = [
    path('news/<int:id>/', news_detail, name = "detail_news")
]