from django import forms

from .models import post_Comments

class comment_form(forms.ModelForm):
    class Meta:
        model = post_Comments
        fields = ['author', 'author_email', 'comment_content']