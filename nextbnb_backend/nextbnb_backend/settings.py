import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY SETTINGS
SECRET_KEY = os.environ.get("SECRET_KEY")

# Debug Mode 설정 (배포 환경에서는 반드시 False)
DEBUG = os.environ.get("DEBUG", "False") == "True"

# IP 주소 및 도메인 추가
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "34.48.2.107"]

# AUTHENTICATION
AUTH_USER_MODEL = 'useraccount.User'

SITE_ID = 1

# CHANNEL LAYERS
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}

# JWT 설정
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKEN": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    "SIGNING_KEY": "acomplexkey",
    "ALOGRIGTHM": "HS512",
}

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# CORS 설정
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'http://34.48.2.107',  # Google Cloud VM의 IP 주소
]

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'http://34.48.2.107',  # Google Cloud VM의 IP 주소
]

# CORS를 모든 도메인에서 허용 (선택 사항, 보안 주의)
CORS_ALLOW_ALL_ORIGINS = False

# STATIC/MEDIA 설정
STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Database 설정
DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        'NAME': os.environ.get("SQL_DATABASE", "nextbnb"),
        'USER': os.environ.get("SQL_USER", "postgresuser"),
        'PASSWORD': os.environ.get("SQL_PASSWORD", "postgrespassword"),
        'HOST': os.environ.get("SQL_HOST", "db"),
        'PORT': os.environ.get("SQL_PORT", "5432"),
    }
}

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
