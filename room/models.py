from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    is_group=models.BooleanField(default=True,blank=True)
    members=models.ManyToManyField(User,related_name='rooms', blank=True)
    def __str__(self):
        return self.name
    
class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)