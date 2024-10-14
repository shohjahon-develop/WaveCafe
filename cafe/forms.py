from django import forms
from.models import Contact,Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user','body']

class ContactForms(forms.ModelForm):


    class Meta:
        model = Contact
        fields = "__all__"