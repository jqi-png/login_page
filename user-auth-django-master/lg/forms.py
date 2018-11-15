from django import forms
from django.forms.models import ModelForm
from .models import UserProfile

CHOICES = (
    ('TE', 'test engineer'),
    ('OP', 'operator'),
    )

class UserForm(ModelForm):
    role = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = UserProfile
        fields = ('email', 'barcode','role')
