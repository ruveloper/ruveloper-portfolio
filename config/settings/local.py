from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = env("DEBUG", default=True)
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="pcq=6!i98hy=byg55_9^os2n!t8-4m84xh$=r2^**8ydpc@5$e"
)
ALLOWED_HOSTS = ["*"]

# DATABASE
# ---------------------------------------------------------------------------
DATABASES = {"default": env.db_url("DATABASE_URL", default="sqlite:///db.sqlite3")}

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env("DJANGO_DEFAULT_FROM_EMAIL", default="noreply@example.com")
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default="root@example.com")
EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[Django] ",
)
# Custom setting, who which receive not automatic email from platform
RECIPIENT_ADDRESS = env.list(
    "RECIPIENT_ADDRESS",
    default=["contact@localhost"],
)

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# We can show emails in console instead of connect to SMTP.
# Alternative we can configure an SMTP backend using the enviroment variables like production
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)
if EMAIL_BACKEND == "django.core.mail.backends.smtp.EmailBackend":
    EMAIL_HOST = env("DJANGO_EMAIL_HOST")
    EMAIL_PORT = env(
        "DJANGO_EMAIL_PORT", default=587
    )  # Recommend use always 587 for TLS connection
    EMAIL_USE_TLS = env(
        "DJANGO_EMAIL_TLS", default=True
    )  # If port is 587 use TLS, if port is 465 use EMAIL_USE_SSL
    EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD")

EMAIL_TIMEOUT = 5

# * Google Analytics / Tag Manager
# * ------------------------------------------------------------------------------
GOOGLE_TAG_ID = env("GOOGLE_TAG_ID")

# * Google reCaptcha v3
# * ------------------------------------------------------------------------------
RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY")
RECAPTCHA_REQUIRED_SCORE = env.float("RECAPTCHA_REQUIRED_SCORE")

# ---------------------------------------------------------------------------
# Tailwind
# ---------------------------------------------------------------------------
TAILWIND_APP_NAME = "apps.website"
INTERNAL_IPS = [
    "127.0.0.1",
]
NPM_BIN_PATH = env.path("NPM_BIN_PATH")  # windows: NodeJS\path\npm.cmd without spaces
