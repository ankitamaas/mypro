# serializers.py
from rest_framework import serializers
from .models import BotKnowledge

class BotKnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotKnowledge
        fields = ['id', 'keyword', 'response']
