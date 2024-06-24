"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
# from decouple import config
import environ
from pathlib import Path
from datetime import timedelta
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

env = environ.Env()
environ.Env.read_env()  # lit les variables d'environnement depuis le fichier .env

CLIENT_ID = env('CLIENT_ID')
CLIENT_SECRET = env('CLIENT_SECRET')
REDIRECT_URI = env('API_42_REDIRECT_URI')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6=yy^n^#kok)4$_&-le2bs7_iytn3fw!fv6y=632e$=0f%3$0y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

## DOMAINE AND HOST FOR THE API
DOMAIN = os.getenv('DOMAIN')
IP = os.getenv('IP')

URL_DOMAIN = f"https://{DOMAIN}:8000"
URL_IP = f"https://{IP}:8000"

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'transcendence.42.fr']
CORS_ORIGIN_ALLOW_ALL=True

# # PROTECTION XSS WITH CORS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "https://localhost:8000",
    "https://127.0.0.1:8000",
]

CSRF_TRUSTED_ORIGINS = ['https://127.0.0.1:8000', 'https://localhost:8000']

CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
CORS_ALLOW_HEADERS = [
    'content-type',
    'origin',
    'x-csrftoken',
    'x-requested-with',
    'accept',
    'authorization',
    'x-csrftoken'
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Application definition

INSTALLED_APPS = [
	'website',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.middleware.csrf', # pour les crsf tokens
	# 'corsheaders',
	'rest_framework',
	'rest_framework.authtoken',
	'rest_framework_simplejwt',  # JWT library
    'pyotp',
	'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    'two_factor',
    'qrcode',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	'django_otp.middleware.OTPMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.joinpath('templates'), # <--- ajoutez cette ligne
        ],
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

# ASGI application for websocket and asyncronous tasks

ASGI_APPLICATION = 'backend.asgi.application'
WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = { 
  'default' : { 
    #'ENGINE' : 'django.db.backends.postgresql_psycopg2',
    'ENGINE': 'django.db.backends.postgresql',
    'HOST' : os.environ.get('POSTGRES_HOST'), 
    'NAME' : os.environ.get('POSTGRES_DB'), 
    'USER' : os.environ.get('POSTGRES_USER'), 
    'PASSWORD' : os.environ.get('POSTGRES_PASSWORD'),
    'PORT': '5432', 
  } 
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
		'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=2),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# Internationalization
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'fr'

LANGUAGES = [
    ('fr', _('French')),
    ('en', _('English')),
    ('ar', _('Arabic')),
    ('uy', _('Uyghur')),
]

LANGUAGE_COOKIE_NAME = 'django_language'

LOCALE_PATHS = [
    BASE_DIR.joinpath('locale'),

]

TIME_ZONE = 'Europe/Paris'

USE_L10N = True

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/media/'
STATIC_ROOT = '/var/www/static/'
STATICFILES_DIRS = [
    BASE_DIR / 
	    'website/static/',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'website.CustomUser'

#LOGIN_URL = 'login'

# Utiliser le header HTTP X-XSS-Protection
#SECURE_BROWSER_XSS_FILTER = True
#SECURE_CONTENT_TYPE_NOSNIFF = True
# settings.py
CLIENT_ID = 'u-s4t2ud-090f3351a6ed650b00f912397184ee17acab63d317231bc0279fb8b5d532e587'
CLIENT_SECRET = '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'
REDIRECT_URI = 'https://127.0.0.1:8000/handle-42-redirect/'
## Définir SECURE_PROXY_SSL_HEADER si vous utilisez un proxy inverse comme Nginx
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

## Rediriger les requêtes HTTP vers HTTPS
SECURE_SSL_REDIRECT = False

## Utiliser des cookies sécurisés
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Configuration HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


