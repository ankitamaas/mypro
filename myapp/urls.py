# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chatbot_response, name='chatbot_response'),  # API endpoint for chatbot response
    path('chatbot/', views.chatbot_page, name='chatbot_page'),  # Chatbot HTML page
]
