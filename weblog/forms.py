from django import forms

from models import Comments

class comment_form(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_author', 'comment_author_email', 'comment_content ']