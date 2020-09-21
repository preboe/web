from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput

class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date']


        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            })
        }

        widgets = {
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            })
        }

        widgets = {
            "date": DateTimeInput(attrs={
                'class': 'form-control'
            })
        }

        widgets = {
            "full_text": DateTimeInput(attrs={
                'class': 'form-control'
            })
        }


