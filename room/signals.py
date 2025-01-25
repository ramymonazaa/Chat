from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Room
from django.shortcuts import render
@receiver(pre_save, sender=Room)
def my_handler(sender,instance, **kwargs):
    print("Signal triggered for Room model!")
    if instance.id:
        print("Existing room is being updated.")
    else:
        print("A new room is being added.")