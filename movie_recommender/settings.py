"""
Django settings for movie_recommender project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import environ
import dj_database_url
env = environ.Env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-4s(=@q9f!p13yun!p$2_v6=7lc2lg_nxr+vwil4737-3en3$2v"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["web-production-24d6.up.railway.app", "127.0.0.1", "nextwatch-mevm.onrender.com"]
CSRF_TRUSTED_ORIGINS = ['https://web-production-24d6.up.railway.app', 'https://127.0.0.1', "https://nextwatch-mevm.onrender.com"]
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "movies",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "movie_recommender.urls"

import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add this line
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

WSGI_APPLICATION = "movie_recommender.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'movie_rec',
#         'USER': 'postgres',
#         'PASSWORD': '200256',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
DATABASE_URL = 'postgresql://movie_rec_user:iLFzxvdsX72WOIrePu6WftIRYq1gdOdO@dpg-cqoeceaj1k6c73b3rjpg-a.oregon-postgres.render.com/movie_rec'
DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL),
}

# DATABASES = {
# 'default': dj_database_url.config(default='postgresql://postgres:wbQrjbetQyBzrcvicsPmuMYlKjPpPuPg@postgres.railway.internal:5432/railway',conn_max_age=1800)
# }

# ENVIRONMENT = env('ENVIRONMENT', default='development')

# POSTGRES_LOCALLY = True
# if ENVIRONMENT == 'production' or POSTGRES_LOCALLY == True:
#     DATABASES['default'] = dj_database_url.parse('postgresql://postgres:wbQrjbetQyBzrcvicsPmuMYlKjPpPuPg@postgres.railway.internal:5432/railway')

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'movies', 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage' 
