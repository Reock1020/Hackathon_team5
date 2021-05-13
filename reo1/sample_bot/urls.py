from .views import home , bot_response
from django.urls import path 

urlpatterns = [
    path('', home, name = 'name'),
		path('bot_response/', bot_response, name = 'bot_response'),
]
