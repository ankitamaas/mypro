# views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BotKnowledge
from .serializers import BotKnowledgeSerializer
from django.views.decorators.csrf import csrf_exempt

# API View to handle chatbot responses
@csrf_exempt
@api_view(['POST'])
def chatbot_response(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON request body
            user_message = request.data.get('message', '').lower()  # Convert message to lowercase for matching
        except (ValueError, KeyError):
            # Handle invalid JSON format
            return Response({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)

        # Search for an exact match in the database
        knowledge = BotKnowledge.objects.filter(keyword__icontains=user_message).first()


        if knowledge:
            # If a match is found, return the corresponding response
            bot_response = knowledge.response
        else:
            # If no exact match is found, attempt a related response (based on the first word)
            related_knowledge = BotKnowledge.objects.filter(keyword__icontains=user_message.split()[0]).first()

            if related_knowledge:
                bot_response = f"{related_knowledge.response}"
            else:
                # If no related response is found, default response
                bot_response = "Sorry, I don't understand that. Could you please rephrase?"
 
        return Response({'response': bot_response})

# View to render the chatbot page (HTML)
def chatbot_page(request):
    return render(request, 'chatbot.html')
