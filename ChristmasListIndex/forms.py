from django import forms
from .models import GiftIdea

class GiftIdeaForm(forms.ModelForm):

    class Meta:
        model = GiftIdea
        fields = ['title', 'description', 'image', 'link', 'suggested_amount']

