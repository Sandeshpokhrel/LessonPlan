from .common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0q5(!y48y5znve2tyt7*-qj^ux#zk3)3cw)$g_20zs(%r)9)qz'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOST = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}