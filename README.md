# 🏠 Backend Django - Imóveis API

API REST para gerenciamento de imóveis com banco de dados PostgreSQL.

## 🚀 Deployment (Render + Vercel)

### **URLs em Produção:**
- **Backend**: https://rodolfo-backend-1.onrender.com/
- **Frontend**: https://rodolfovelosocorretor.vercel.app/

---

## 📦 Instalação Local

### 1. **Clone o repositório**
```bash
git clone seu-repo
cd backend
```

### 2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. **Instale dependências**
```bash
pip install -r requirements.txt
```

### 4. **Configure as variáveis de ambiente**
```bash
cp .env.example .env.local
# Edite .env.local com suas configurações
```

### 5. **Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. **Crie um superusuário**
```bash
python manage.py createsuperuser
```

### 7. **Execute o servidor**
```bash
python manage.py runserver
```

Acesse: http://localhost:8000/

---

## 🧪 Testando a API

### **Endpoints Disponíveis:**

#### GET - Listar todos os imóveis
```bash
curl http://localhost:8000/api/imoveis/
```

#### GET - Detalhe de um imóvel
```bash
curl http://localhost:8000/api/imoveis/1/
```

#### POST - Criar novo imóvel
```bash
curl -X POST http://localhost:8000/api/imoveis/ \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Casa em JP",
    "descricao": "Descrição...",
    "preco": 500000,
    "cidade": "João Pessoa",
    "bairro": "Tambaú",
    "quartos": 3,
    "banheiros": 2,
    "vagas": 2,
    "metragem": 150,
    "tipo": "casa",
    "finalidade": "venda"
  }'
```

---

## 🔧 Configurações Importantes

### **settings.py:**
- `DEBUG=False` em produção
- `ALLOWED_HOSTS` inclui o domínio Render
- `WHATSAPP_NUMBER` configurável via variáveis de ambiente
- CORS habilitado para Vercel
- PostgreSQL em produção (SQLite local)

### **Variáveis de Ambiente (Render):**
```
SECRET_KEY=sua-chave-secreta
DB_PASSWORD=sua-senha-postgres
DATABASE_URL=postgresql://user:pass@host/db
WHATSAPP_NUMBER=5583987654321
CLOUDINARY_CLOUD_NAME=seu-cloud-name
CLOUDINARY_API_KEY=sua-api-key
CLOUDINARY_API_SECRET=sua-api-secret
```

---

## 📚 Estrutura do Projeto

```
backend/
├── backend/              # Configurações Django
│   ├── settings.py       # Configurações
│   ├── urls.py           # URLs principais
│   └── wsgi.py          # WSGI
├── imoveis/             # App de imóveis
│   ├── models.py        # Modelos
│   ├── views.py         # Views API
│   ├── urls.py          # URLs app
│   └── templates/       # HTML
├── manage.py
├── requirements.txt
├── build.sh            # Script Render
└── render.yaml         # Configuração Render
```

---

## �️ Armazenamento de Imagens

### **Cloudinary (Recomendado para Produção)**

O projeto usa **Cloudinary** para armazenar imagens porque:

- ✅ **Render não persiste arquivos** entre deploys
- ✅ **PostgreSQL gratuito** não armazena arquivos binários
- ✅ **Cloudinary oferece 25GB grátis** + 25k uploads/mês

### **Configuração do Cloudinary:**

1. **Crie conta gratuita**: https://cloudinary.com/
2. **Pegue suas credenciais** no Dashboard
3. **Configure no Render**:
   ```
   CLOUDINARY_CLOUD_NAME=seu-cloud-name
   CLOUDINARY_API_KEY=sua-api-key
   CLOUDINARY_API_SECRET=sua-api-secret
   ```

### **Desenvolvimento Local:**
- Sem Cloudinary: imagens ficam em `media/` local
- Com Cloudinary: imagens vão para a nuvem

---

## �🐛 Troubleshooting

### Erro 500 ao acessar `/api/imoveis/`
- Verificar `ALLOWED_HOSTS`
- Verificar `DEBUG=False` em produção
- Checar logs: `python manage.py runserver`

### Imagens não aparecem
- Executar: `python manage.py collectstatic`
- Verificar `MEDIA_URL` e `MEDIA_ROOT`

### CORS error
- Verificar `CORS_ALLOWED_ORIGINS`
- Confirmar `CORS_ALLOW_CREDENTIALS = True`

---

## 🔐 Segurança

- ✅ CSRF_TRUSTED_ORIGINS configurado
- ✅ CORS restrito aos domínios autorizados
- ✅ SECRET_KEY via variáveis de ambiente
- ✅ SSL/TLS em produção (Render)

---

## 📝 To-Do

- [ ] Adicionar autenticação de API (Token)
- [ ] Implementar paginação
- [ ] Adicionar filtros e busca
- [ ] Melhorar documentação Swagger

---

Desenvolvido com ❤️
