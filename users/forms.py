from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =  ['content'] 

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback_Post
        fields =  ['name', 'email', 'content']