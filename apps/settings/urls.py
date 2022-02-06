from django.urls import path 
from apps.settings.views import index, about_us 


urlpatterns = [
    path('about_us/', about_us, name = "about_us"),
    path('', index, name="index")
]