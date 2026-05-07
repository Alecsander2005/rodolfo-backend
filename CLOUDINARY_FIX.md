# 🐛 Solução: Erro 500 ao criar Imóvel com Imagem

## Problema
Ao tentar criar ou editar um imóvel com imagem, você recebia um erro **500** com a mensagem:
```
Invalid cloud_name Root
```

## Causa Raiz
O arquivo `.env` tinha a variável `CLOUDINARY_CLOUD_NAME` configurada incorretamente:

```env
CLOUDINARY_CLOUD_NAME =Root   # ❌ ERRADO - espaços e letra maiúscula
```

O Cloudinary rejeitava essa configuração porque:
1. **Espaço antes do `=`**: Python carrega como variável inválida
2. **Espaço depois do `=`**: O valor fica como `" Root "` em vez de `"Root"`
3. **Letra maiúscula**: Cloud Names do Cloudinary devem estar em minúsculas

## Solução Aplicada ✅

Corrigi o arquivo `.env` para:
```env
CLOUDINARY_CLOUD_NAME=root
CLOUDINARY_API_KEY=748696595978947
CLOUDINARY_API_SECRET=pnQFRWt4XEZYxWiQDVCwR3xebsw
```

## ⚠️ Próximas Ações

### 1. **Verificar o Cloud Name Correto**
O valor `root` pode não ser seu Cloud Name real. Para verificar:
- Acesse sua conta no [Cloudinary Dashboard](https://cloudinary.com/console)
- Seu Cloud Name está na página inicial, exemplo: `d1a2b3c4d5`
- Substitua `root` pelo seu Cloud Name real

### 2. **Atualizar o `.env` em Produção**
Certifique-se que o arquivo `.env` no servidor de produção (Render) tem o Cloud Name correto:

```env
CLOUDINARY_CLOUD_NAME=seu_cloud_name_real
CLOUDINARY_API_KEY=sua_api_key
CLOUDINARY_API_SECRET=seu_api_secret
```

### 3. **Reiniciar a Aplicação**
Após atualizar as variáveis de ambiente em produção:
- Faça um redeploy no Render
- Ou reinicie a aplicação Django

### 4. **Testar**
Tente criar/editar um imóvel com uma imagem - deve funcionar agora! ✅

## 📝 Boas Práticas para Evitar Isso Novamente

1. **Use um validador de `.env`**
   ```python
   # No settings.py, adicione após carregar as variáveis:
   if not os.getenv('CLOUDINARY_CLOUD_NAME'):
       raise ImproperlyConfigured(
           "CLOUDINARY_CLOUD_NAME não está configurado. "
           "Verifique seu arquivo .env"
       )
   ```

2. **Remova espaços em variáveis de ambiente**
   ```env
   # ❌ Errado
   CHAVE = valor
   
   # ✅ Correto
   CHAVE=valor
   ```

3. **Use lowercase para Cloud Names**
   ```env
   # ✅ Correto
   CLOUDINARY_CLOUD_NAME=meu_cloud_name
   ```

## Referências
- [Documentação Cloudinary Python SDK](https://cloudinary.com/documentation/cloudinary_basics)
- [Django Cloudinary Storage](https://github.com/klis87/django-cloudinary-storage)
