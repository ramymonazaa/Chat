from django import forms
from django.contrib.auth.models import User
from .models import Room
from .middleware import get_current_user
class RoomForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    user = get_current_user()
    if user:
        print(f"User: {user.username}, ID: {user.id}")
    else:
        print("No user available.")
    class Meta:
        model = Room
        fields = ['name', 'members']
