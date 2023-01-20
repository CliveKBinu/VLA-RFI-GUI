"""Django settings for rfi_query project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from getpass import getuser
from pathlib import Path

import environ

from email.utils import getaddresses


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SETTINGS_DIR = Path(__file__).resolve().parent

_user = getuser()
env = environ.Env(
    DEBUG=(bool, True),
    ALLOWED_HOSTS=(list, []),
    INTERNAL_IPS=(list, []),
    SENTRY_ENV=(str, f"{_user}_dev"),
    STATIC_ROOT=(str, None),
)
_env_file_template_path = Path(SETTINGS_DIR, ".env.template")
_default_env_file_path = Path(SETTINGS_DIR, ".env")
_env_file_path = env.str("ENV_PATH", _default_env_file_path)
if not Path(_env_file_path).exists():
    raise ValueError(
        f"You must create a .env file at {_default_env_file_path} "
        f"(use {_env_file_template_path} as a template), "
        "or specify another path via the ENV_PATH variable"
    )
try:
    with open(_env_file_path):
        pass
except PermissionError as error:
    raise PermissionError(
        f"You do not have permission to read {_env_file_path}. Please contact gbosdd@nrao.edu"
        "if this is in error"
    ) from error
environ.Env.read_env(_env_file_path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

# set up the email logs
ADMINS = getaddresses([env("DJANGO_ADMINS")])

# CONN_MAX_AGE = None

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "django_extensions",
    "crispy_forms",
    "legacy_rfi",
    "rfi",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "rfi_query.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "rfi_query.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": env.db("DJANGO_DB"),
    "legacy_rfi": env.db("LEGACY_RFI_DB"),
}

DATABASE_ROUTERS = [
    "rfi_query.db_routers.LegacyRfiRouter",
]


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = env("STATIC_ROOT")
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

APPEND_SLASH = True
### Non-Django Settings

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}

### DJANGO-DEBUG-TOOLBAR
INTERNAL_IPS = ["127.0.0.1", "192.33.116.243"]

CRISPY_TEMPLATE_PACK = "bootstrap4"
