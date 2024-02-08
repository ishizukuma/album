from django import forms

class MessageForm(forms.Form):
    content = forms.CharField()
