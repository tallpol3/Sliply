import os

import environ
root = environ.Path(__file__) - 2 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),) # set default values and casting
environ.Env.read_env(env_file=root('.env')) # reading .env file

BASE_DIR = root()

DEBUG = env('DEBUG') # False if not in os.environ
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = env('SECRET_KEY') # Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ

DATABASES = {
    'default': env.db(), # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ROOT_URLCONF = 'sliply_project.urls'
WSGI_APPLICATION = 'sliply_project.wsgi.application'
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='redis://redis:6379/')

SOCIAL_AUTH_FACEBOOK_KEY = env('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = env('SOCIAL_AUTH_FACEBOOK_SECRET')


ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_SSL = env('EMAIL_USE_SSL')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_REDIRECT_URL = 'main'


INSTALLED_APPS = [
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'oauth2_provider',
    'rest_framework_social_oauth2',
    'sslserver',
    'sliply',
    'rest_framework',
    'rest_framework.authtoken',
    'sliply_api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['sliply/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}