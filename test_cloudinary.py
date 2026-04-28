#!/usr/bin/env python
"""
Script para testar configuração do Cloudinary
Execute: python test_cloudinary.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

def test_cloudinary():
    print("🖼️  Testando configuração do Cloudinary...\n")

    try:
        import cloudinary
        print("✅ Cloudinary importado com sucesso")

        # Verifica se as credenciais estão configuradas
        cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME')
        api_key = os.environ.get('CLOUDINARY_API_KEY')
        api_secret = os.environ.get('CLOUDINARY_API_SECRET')

        if cloud_name and api_key and api_secret:
            print("✅ Credenciais do Cloudinary encontradas")
            print(f"   Cloud Name: {cloud_name}")

            # Testa conexão
            try:
                result = cloudinary.api.ping()
                print("✅ Conexão com Cloudinary OK")
                print(f"   Status: {result.get('status', 'unknown')}")
            except Exception as e:
                print(f"❌ Erro na conexão: {e}")

        else:
            print("⚠️  Credenciais do Cloudinary não encontradas")
            print("   Modo: Desenvolvimento local (FileSystem)")
            print("   Imagens serão salvas em: media/")

        # Verifica DEFAULT_FILE_STORAGE
        from django.conf import settings
        storage = settings.DEFAULT_FILE_STORAGE
        print(f"✅ Storage configurado: {storage}")

        if 'cloudinary' in storage.lower():
            print("✅ Usando Cloudinary para produção")
        else:
            print("✅ Usando FileSystem para desenvolvimento")

    except ImportError:
        print("❌ Cloudinary não instalado")
        print("   Execute: pip install cloudinary django-cloudinary-storage")

    print("\n🎉 Teste concluído!")

if __name__ == '__main__':
    test_cloudinary()