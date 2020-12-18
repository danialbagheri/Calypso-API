"""
Django settings for calypso project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

import os

PRODUCTION_ENVIRONMENT = os.environ['PRODUCTION_ENVIRONMENT'] == 'TRUE'

if PRODUCTION_ENVIRONMENT:
    try:
        # this production_settings.py is kept off github to keep the secret key secret
        from .production import *
    except ImportError:
        pass
else:
    # it's development

    try:
        from .development import *
    except ImportError:
        pass

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
SHOPIFY_API_KEY = os.environ.get('SHOPIFY_API_KEY', None)
SHOPIFY_PASSWORD = os.environ.get('SHOPIFY_PASSWORD', None)
API_VERSION = "2020-10"
SHOPIFY_URL = "https://%s:%s@lincocare.myshopify.com/admin/api/%s" % (
    SHOPIFY_API_KEY, SHOPIFY_PASSWORD, API_VERSION)
DRF_RECAPTCHA_SECRET_KEY = os.environ.get('DRF_RECAPTCHA_SECRET_KEY', None)
# DRF_RECAPTCHA_DOMAIN = "127.0.0.1:8000"
DRF_RECAPTCHA_PROXY = {
    'http': 'http://127.0.0.1:8000',
    'https': 'https://127.0.0.1:8000',
    'https': 'https://34ce4fe2bd40.ngrok.io'
}
# product = shopify.Product.find( title = "Scalp protection" )
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django_grapesjs',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phonenumber_field',
    'django_summernote',
    'corsheaders',
    'crispy_forms',
    'web',
    'product',
    'blog',
    'page',
    'review',
    'dashboard',
    'django.contrib.sitemaps',
    'rest_framework',
    'drf_recaptcha',
    'ordered_model',
    'django.contrib.sites',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'calypso.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'calypso.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %y',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        # 'calypso.throttling.PostAnonymousRateThrottle',
        'calypso.throttling.PutAnonymousRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10000/day',
        'user': '1000000/day',
        # 'post_anon':'3/minute',
        'put_anon':'2/minute',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'GB'

USE_I18N = True

USE_L10N = True

USE_TZ = True

X_FRAME_OPTIONS = 'SAMEORIGIN'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_root'),
    os.path.join(BASE_DIR, 'node/dist'),
]
# The full path on the system
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TEMPLATES_ROOT = os.path.join(BASE_DIR, 'templates')
GRAPESJS_DEFAULT_HTML =  os.path.join(TEMPLATES_ROOT ,'django_grapesjs/default.html')

ADMINS = [
    ('Danial', 'danial@lincocare.com'),
]
MANAGERS = [
    ('Danial', 'danial@lincocare.com'),
]
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

CORS_ORIGIN_ALLOW_ALL = True
# TODO: to be deleted on the live server
CORS_ALLOWED_ORIGINS = (
    'http://127.0.0.1:3000',
    'http://127.0.0.1:8000',
    'http://localhost:3000',
)
CRISPY_TEMPLATE_PACK = 'bootstrap4'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
DATA_UPLOAD_MAX_MEMORY_SIZE = 9437184
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
EMAIL_SUBJECT_PREFIX = "Calypso Sun - "
DEFAULT_FROM_EMAIL = "info@calypsosun.com"
SERVER_EMAIL = "info@calypsosun.com"
SITE_ID = 1
PHONENUMBER_DB_FORMAT = "NATIONAL"
PHONENUMBER_DEFAULT_REGION = "GB"
SUMMERNOTE_THEME = 'bs4'  # Show summernote with Bootstrap4
SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'focus': True,
        'fontSizes': ['8', '9', '10', '11', '12', '14', '18', '22', '24', '36', '48', '64', '82', '150'],
        'width': '100%',
        'height': '400px',
        'prettifyHtml': True,
        'toolbar': [
            ['undo', ['undo', ]],
            ['redo', ['redo', ]],
            ['style', ['style']],
            ['fontsize', ['fontsize']],
            ['font', ['bold', 'italic', 'clear', 'strikethrough', 'underline', ]],
            ['fontname', ['fontname']],
            ['color', ['forecolor', 'backcolor', 'color']],
            ['misc', ['link', 'picture', 'print', 'help', ]],
            ['para', ['ul', 'ol', 'paragraph']],
            ['view', ['fullscreen', 'codeview']],
            ['cleaner', ['cleaner']],
        ],
        'codemirror': {  # codemirror options
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            'theme': 'monokai',
            'smartIndent': True,
            'lineWrapping': True,
            'spellcheck': True,
        },
        'cleaner': {
            'action': 'button',
            'newline': '<br>',  # Summernote's default is to use '<p><br></p>'
            'notStyle': 'position:absolute;top:0;left:0;right:0',  # Position of Notification
            'icon': '<i class="note-icon">CLEAN STYLE</i>',
            'keepHtml': True,  # Remove all Html formats
            # If keepHtml is true, remove all tags except these
            'keepOnlyTags': ['<p>', '<br>', '<ul>', '<li>', '<b>', '<strong>', '<i>', '<a>', '<span>', '</br>', '<style>', '<ol>'],
            'keepClasses': True,  # Remove Classes
            # Remove full tags with contents
            'badTags': ['script', 'applet', 'embed', 'noframes', 'noscript', 'html'],
            # Remove attributes from remaining tags
            'badAttributes': ['start'],
            'limitChars': False,  # 0/false|# 0/false disables option
            'limitDisplay': 'both',  # text|html|both
            'limitStop': False  # true/false
        }
    },
    'css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/theme/monokai.min.css',
    ),
    # 'js_for_code_highlight': (  # Also for SummernoteInplaceWidget
    #     os.path.join(STATIC_URL, '/summernote/summernote-ext-highlight.js'),
    # ),
}
