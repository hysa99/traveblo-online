from django.db import models
from item.models import Item
from django.contrib.auth.models import User







# Create your models here.

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    published_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-modified_at',)




class ConversationMessages(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    published_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
