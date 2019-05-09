from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']

# class ContactForm(forms.Form):
#     name=forms.CharField()
#     message=forms.CharField(width=forms.Textarea)
    
#     def send_email(self):
#         pass