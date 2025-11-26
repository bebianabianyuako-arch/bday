import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-randomstring' # Biarkan saja ini

# VERCEL/PRODUCTION SETTINGS
DEBUG = False # Wajib False di Production
ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    # Kita hanya butuh static files, yang lain dihapus karena butuh database
    'django.contrib.staticfiles',
    'wishes', 
]

# MIDDLEWARE (Versi Stabil Tanpa Database)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # Middleware penting yang tetap harus ada:
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'birthday_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'birthday_project.wsgi.application'

# TIDAK ADA BLOK DATABASES (PENTING! Mencegah error SQLite)

# Password validation
# Dihapus karena tidak ada fitur login/user

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images, Audio, Video)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'