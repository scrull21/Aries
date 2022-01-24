from django.urls import path
from apps.categories.views import category_index, category_detail


urlpatterns = [
    path('categories/', category_index, name = 'category_index'),
    path('category/<str:slug>/', category_detail, name = 'category_detail')
]