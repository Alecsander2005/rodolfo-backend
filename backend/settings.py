import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Segurança
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-temp-key')
DEBUG = False

ALLOWED_HOSTS = ['rodolfo-backend-1.onrender.com', 'localhost', '127.0.0.1', '.onrender.com']

# 🧩 Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',   # 👈 CORS
    'imoveis',
]

# ⚙️ Middlewares
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 👈 TEM QUE SER O PRIMEIRO
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# 🗄️ Database Configuration
if os.environ.get('DATABASE_URL'):
    # Render PostgreSQL - usar URL interna
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'rodolfo_db',
            'USER': 'rodolfo_user',
            'PASSWORD': os.environ.get('DB_PASSWORD', 'nShkJUoFwETH1e8bzjB3j8wgI8ODZ8X6'),
            'HOST': 'dpg-d7nvub9kh4rs73bg1r1g-a',
            'PORT': '5432',
        }
    }
else:
    # Local SQLite (development)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Recife'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 📱 WhatsApp Configuration
WHATSAPP_NUMBER = os.environ.get('WHATSAPP_NUMBER', '5583987654321')  # Número com código do país

# 🌐 CORS (ligação com o Vercel)
CORS_ALLOWED_ORIGINS = [
    "https://rodolfovelosocorretor.vercel.app",
    "http://localhost:3000",  # Para testes locais
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# 🔐 (opcional, mas recomendado se tiver POST/login)
CSRF_TRUSTED_ORIGINS = [
    "https://rodolfovelosocorretor.vercel.app",
    "http://localhost:3000",
]

# 🔒 Segurança em Produção
if not DEBUG:
    SECURE_SSL_REDIRECT = False  # Render gerencia SSL
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_SECURITY_POLICY = {
        "default-src": ("'self'", "https://rodolfovelosocorretor.vercel.app"),
    }