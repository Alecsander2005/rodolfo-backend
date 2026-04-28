#!/bin/bash
# Script para testar a API localmente

echo "🧪 Testando API de Imóveis..."
echo ""

# Teste GET list
echo "1️⃣  GET /api/imoveis/"
curl -X GET http://localhost:8000/api/imoveis/ \
  -H "Content-Type: application/json" \
  --silent | python -m json.tool

echo ""
echo ""

# Teste com ID (ajuste para um ID válido)
echo "2️⃣  GET /api/imoveis/1/"
curl -X GET http://localhost:8000/api/imoveis/1/ \
  -H "Content-Type: application/json" \
  --silent | python -m json.tool

echo ""
echo ""
echo "✅ Testes completos!"
