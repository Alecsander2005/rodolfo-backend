from django import forms
from .models import Imovel

class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ['titulo', 'tipo', 'finalidade', 'status', 'cidade', 'bairro', 'quartos', 'banheiros', 'vagas_garagem', 'metragem', 'preco', 'imagem_principal', 'descricao']
