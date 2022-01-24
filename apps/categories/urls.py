from django.urls import path
from apps.categories.views import category_index


urlpatterns = [
    path('', category_index, name = 'category_index'),
]