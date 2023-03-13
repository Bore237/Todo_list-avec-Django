from django import forms
from .models import *

#Creer un formulaire avec django

class FormTask(forms.ModelForm):
    taches = forms.CharField( max_length=150, 
                             widget=forms.TextInput(attrs={
                             'placeholder': 'Entrer votre taches',
                              'class': 'form-control-lg',
                              'type':'text'
                            }),)
    
    title = forms.CharField( max_length=100, 
                             widget=forms.TextInput(attrs={
                             'placeholder': 'Entrer votre Titre',
                              'class': 'form-control-lg',
                              'type':'text'
                            }),)
    
    class Meta:
        model = Task
        fields = [
            'taches',
            'title'
        ]
