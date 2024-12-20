from django.db import models

class BotKnowledge(models.Model):
    keyword = models.CharField(max_length=255)
    response = models.TextField()

    def __str__(self):
        return self.keyword
