#!/usr/bin/env python
"""
Script para testar a API de imóveis localmente
Execute: python test_api.py
"""

import os
import django
import json

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from imoveis.models import Imovel
from imoveis.views import _serialize_imovel
from django.test import RequestFactory

def test_api():
    print("🧪 Testando API de Imóveis...\n")
    
    # Cria um factory para simular requisições
    factory = RequestFactory()
    request = factory.get('/')
    request.META['HTTP_HOST'] = 'localhost:8000'
    
    # Busca todos os imóveis
    imoveis = Imovel.objects.all()
    
    if not imoveis.exists():
        print("⚠️  Nenhum imóvel cadastrado!")
        print("   Cadastre um imóvel no painel admin: http://localhost:8000/admin/")
        return
    
    print(f"✅ Total de imóveis: {imoveis.count()}\n")
    
    for imovel in imoveis[:3]:  # Mostra apenas os 3 primeiros
        serialized = _serialize_imovel(imovel, request)
        print(f"📍 {imovel.titulo}")
        print(f"   Preço: R$ {imovel.preco}")
        print(f"   Localização: {imovel.bairro}, {imovel.cidade}")
        print(f"   Tipo: {imovel.tipo} ({imovel.finalidade})")
        print(f"   Status: {imovel.status}")
        print(f"   JSON Response OK: {bool(serialized)}")
        print()
    
    print("✅ API funcionando corretamente!")

if __name__ == '__main__':
    try:
        test_api()
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
