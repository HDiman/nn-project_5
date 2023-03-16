from .models import Portfolio
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ["title", "num"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название актива',
            }),
            "num": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кол-во',
            }),
        }
