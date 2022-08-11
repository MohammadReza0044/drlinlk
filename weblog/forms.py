from django import forms

from .models import Comments

class comment_form(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['author', 'author_email', 'comment_content']