from django import forms
from .models import Message



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

    def save(self, commit=True, *args, **kwargs):
        # commit=Falseの場合は一時保存してインスタンスを返す
        instance = super().save(commit=False, *args, **kwargs)
        if commit:
            instance.save()
        return instance
