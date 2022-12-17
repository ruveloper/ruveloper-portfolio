"""
With these settings, tests run faster.
"""
from pathlib import Path

from .base import *  # noqa
from .base import BASE_DIR, env

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = env("DEBUG", default=True)
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="0jj2@a8#01k0cy1q1i1_tljr=y=2pyqmy0k+-h%6gl2jkggh(6",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# INTERNATIONALIZATIONS
# ---------------------------------------------------------------------------
LANGUAGE_CODE = "en"

# MEDIA
# ---------------------------------------------------------------------------
MEDIA_ROOT = Path(BASE_DIR, "media_test")

# DATABASE
# ---------------------------------------------------------------------------
DATABASES = {"default": env.db_url("DATABASE_URL", default="sqlite:///db.sqlite3")}

# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env("DJANGO_DEFAULT_FROM_EMAIL", default="noreply@test.com")
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default="root@test.com")
EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[Django Test] ",
)
# Custom setting, who which receive not automatic email from platform
RECIPIENT_ADDRESS = env.list(
    "RECIPIENT_ADDRESS",
    default=["contact@test.com"],
)

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# * Google Analytics / Tag Manager
# * ------------------------------------------------------------------------------
GOOGLE_TAG_ID = env("GOOGLE_TAG_ID", default="")

# * Google reCaptcha v3
# * ------------------------------------------------------------------------------
RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY", default="")
RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY", default="")
RECAPTCHA_REQUIRED_SCORE = env.float("RECAPTCHA_REQUIRED_SCORE", default=0.85)
