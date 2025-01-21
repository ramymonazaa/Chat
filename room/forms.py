from django import forms
from django.contrib.auth.models import User
from .models import Room

class RoomForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Room
        fields = ['name','slug', 'members']
