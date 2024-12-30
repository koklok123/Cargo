from django import forms

from .models import Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "description", "news")