import os
from pathlib import Path
from dotenv import load_dotenv
import cloudinary
import dj_database_url
from django.core.exceptions import ImproperlyConfigured

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


def get_env(name, default=''):
    value = os.getenv(name, default)
    if isinstance(value, str):
        value = value.strip()
        if name == 'CLOUDINARY_CLOUD_NAME':
            value = value.lower()
    return value


SECRET_KEY = get_env('SECRET_KEY')
if not SECRET_KEY:
    raise ImproperlyConfigured('SECRET_KEY não está configurado.')

DEBUG = False

ALLOWED_HOSTS = [
    'rodolfo-backend-1.onrender.com',
    '.onrender.com',
    'localhost',
    '127.0.0.1',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',

    'cloudinary',
    'cloudinary_storage',

    'imoveis',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
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


# ==========================
# BANCO DE DADOS SUPABASE
# ==========================

DATABASE_URL = get_env('DATABASE_URL')

if not DATABASE_URL:
    raise ImproperlyConfigured('DATABASE_URL não está configurada.')

DATABASES = {
    'default': dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        ssl_require=True
    )
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Recife'

USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': get_env('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': get_env('CLOUDINARY_API_KEY'),
    'API_SECRET': get_env('CLOUDINARY_API_SECRET'),
}

cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=CLOUDINARY_STORAGE['API_KEY'],
    api_secret=CLOUDINARY_STORAGE['API_SECRET'],
)

if not CLOUDINARY_STORAGE['CLOUD_NAME']:
    raise ImproperlyConfigured(
        'CLOUDINARY_CLOUD_NAME não está configurado.'
    )

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    "https://rodolfovelosocorretor.vercel.app",
    "http://localhost:3000",
]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "https://rodolfovelosocorretor.vercel.app",
]

SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

WHATSAPP_NUMBER = get_env('WHATSAPP_NUMBER')