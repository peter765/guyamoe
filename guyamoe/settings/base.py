"""
Django settings for guyamoe project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import subprocess
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
PARENT_DIR = BASE_DIR.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "/bB/PiOBQ+4sm9nugkW5Oj5e9JvRKNPRIfNt1P6XSm0=")

CANONICAL_ROOT_DOMAIN = "localhost:8000"

DEBUG = True

ALLOWED_HOSTS = ["localhost", "hachirumi.mooo.com"]

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    "api.apps.ApiConfig",
    "reader.apps.ReaderConfig",
    "homepage.apps.HomepageConfig",
    "misc.apps.MiscConfig",
    "proxy.apps.ProxyConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
]

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

INTERNAL_IPS = ("127.0.0.1",)

ROOT_URLCONF = "guyamoe.urls"

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
#         "LOCATION": "unique-snowflake",
#     }
# }

CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache",}}

MIDDLEWARE = [
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "homepage.middleware.ReferralMiddleware",
]

# REFERRAL_SERVICE = 'http://127.0.0.1:8080' # Change this to where-ever Ai is hosted

ROOT_URLCONF = "guyamoe.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "guyamoe.context_processors.branding",
                "guyamoe.context_processors.home_branding",
                "guyamoe.context_processors.urls",
            ],
        },
    },
]

WSGI_APPLICATION = "guyamoe.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_global"),
    # os.path.join(BASE_DIR, "homepage", "static"),
    # os.path.join(BASE_DIR, "reader", "static"),
]

STATIC_VERSION = "?v=" + subprocess.check_output(
    ["git", "-C", str(BASE_DIR), "rev-parse", "--short", "HEAD"], text=True
)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


IMGUR_CLIENT_ID = os.environ.get("IMGUR_CLIENT_ID", "")
MAIL_DISCORD_WEBHOOK_ID = int(os.environ.get("MAIL_DISCORD_WEBHOOK_ID", 1))
MAIL_DISCORD_WEBHOOK_TOKEN = os.environ.get("MAIL_DISCORD_WEBHOOK_TOKEN", "")

BRANDING_NAME = "Hachirumi"
BRANDING_DESCRIPTION = "Thank you for reading! A circle that works on random twitter and pixiv one-shots and the occasional cute manga."
BRANDING_IMAGE_URL = "http://hachirumi.mooo.com/static/img/tumbnail.png"

HOME_BRANDING_NAME = "Home for scanlations of Hachirumi"
HOME_BRANDING_DESCRIPTION = "Read our latest chapters here."
HOME_BRANDING_IMAGE_URL = "http://hachirumi.mooo.com/static/img/tumbnail.png"

IMAGE_PROXY_URL = "https://proxy.f-ck.me"
