from django import forms
from meuApp.models import Produto

class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'categoria', 'imagem']