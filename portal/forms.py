from django import forms
from portal.models import Autor, Editora, Livro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor #referencia qual model esse forme vai utilizar
        fields = ('nome', 'data_nascimento', 'email') #ou exclude()
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'data_nascimento': forms.DateInput(attrs= {'class': 'form-control'}),
            'email': forms.EmailInput(attrs= {'class': 'form-control'}),
        }

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ('nome', 'cidade', 'estado')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),

        }


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'editora': forms.Select(attrs={'class': 'form-control'}),
            'formato': forms.Select(attrs={'class': 'form-control'}),
            'data_lancamento': forms.DateInput(attrs= {'class': 'form-control'}),
            'numero_paginas': forms.NumberInput(attrs= {'class': 'form-control'}),

        }