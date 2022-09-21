from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = env("DEBUG", default=False)
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

# DATABASES
# ------------------------------------------------------------------------------
DATABASES = {"default": env.db_url("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa F405
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # noqa F405

# PRODUCTION APPS
# ------------------------------------------------------------------------------
INSTALLED_APPS += []  # noqa F405

# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env("DJANGO_DEFAULT_FROM_EMAIL")
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL")
EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[Django] ",
)
# Custom list setting, who which receive not automatic email from platform
RECIPIENT_ADDRESS = env.list("RECIPIENT_ADDRESS")

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# Use SMTP server on port 587 TLS
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
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

# * SECURE CONFIG
# ! APPLY ONLY when the entire website is correctly runnning over HTTPS Secure on production
# * ------------------------------------------------------------------------------
# * Prevent send cookies over , only HTTPS and prevent read from Javascript with HTTOnly
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

# * Redirect all HTTP to HTTPS
# SECURE_SSL_REDIRECT = True # if NGINX manage redirects, Don't use this.

# * X-XSS-Protection
# Don't use this header --> https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection

# * X-Content-Type-Options
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = True  # Django default -> True

# * Clickjacking Protection
# https://docs.djangoproject.com/en/stable/ref/clickjacking/
X_FRAME_OPTIONS = "DENY"  # Django default -> 'DENY'

# * Referrer-Policy
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
# ! HSTS
# ! BEWARE: After seeing the header, browsers will NOT EASILY LET YOU REVERSE that decision and will
# ! insist on HTTPS over HTTP for the seconds we specify.
# For testing SECURE_HSTS_SECONDS = 30, for production 2592000 (30 days) or 31536000 (1 year - recommend by Django)
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# * SECURE_PROXY_SSL_HEADER
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
