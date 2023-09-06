from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        mode = Review
        fields = ['user', 'rating', 'comment']
