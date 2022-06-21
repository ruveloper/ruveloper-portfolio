"""
Django base settings for portfolio project.
"""

import os
from pathlib import Path
import environ

# DIRECTORIES
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = Path(BASE_DIR, 'apps')

# EVIRONMENT VARIABLES
# ---------------------------------------------------------------------------
env = environ.Env()
env.read_env(Path(BASE_DIR, '.env'))

# APPLICATIONS
# ---------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'solo',
    'widget_tweaks',
    'fontawesomefree',
    'tailwind',
    'django_browser_reload',
    # Compress html and static files
    'django_minify_html',
    'compressor',
    # CMS - CKEditor
    'ckeditor',
    'ckeditor_uploader',
]
LOCAL_APPS = [
    'apps.website.apps.WebsiteConfig'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARES
# ---------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Compress html and static files
    'django_minify_html.middleware.MinifyHtmlMiddleware',

    # Django Browser Reload
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

# TEMPLATES
# ---------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND':'django.template.backends.django.DjangoTemplates',
        'DIRS':[Path(APPS_DIR, 'templates'), Path(APPS_DIR, 'website', 'templates')],
        'APP_DIRS':True,
        'OPTIONS':{
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#built-in-template-context-processors
            'context_processors':[
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# STATIC FILES FINDERS
# ---------------------------------------------------------------------------
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    # Django compressor finder..
    'compressor.finders.CompressorFinder',
)

# ADMIN CONFIGURATIONS
# ---------------------------------------------------------------------------
# Django Admin URL. Its recommend change the URL for Admin on production
ADMIN_URL = env("DJANGO_ADMIN_URL", default="admin/")
ADMINS = [('Ruben Caballero', 'dev.rubencaballero@gmail.com'), ]
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging
# for more details on how to customize logging configuration.
LOGGING = {
    "version":1,
    "disable_existing_loggers":False,
    "formatters":{
        "verbose":{
            "format":"%(levelname)s %(asctime)s %(module)s "
                     "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers":{
        "console":{
            "level":"DEBUG",
            "class":"logging.StreamHandler",
            "formatter":"verbose",
        }
    },
    "root":{"level":"INFO", "handlers":["console"]},
}

# GENERAL
# ---------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# PASSWORD VALIDATIONS
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
# ---------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# INTERNATIONALIZATIONS
# https://docs.djangoproject.com/en/4.0/topics/i18n/
# ---------------------------------------------------------------------------
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# STATIC FILES
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# ---------------------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = Path(BASE_DIR, 'static')
STATICFILES_DIRS = [Path(APPS_DIR, 'website', 'static'), ]

# MEDIA
# ---------------------------------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = Path(BASE_DIR, 'media')

# --------------------------- THIRD-PARTY CONFIG ----------------------------

# Django SOLO
# ---------------------------------------------------------------------------
GET_SOLO_TEMPLATE_TAG_NAME = 'get_singleton'

# CKEditor
# ---------------------------------------------------------------------------
CKEDITOR_UPLOAD_PATH = 'cms/uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_ALLOW_NONIMAGE_FILES = False  # No allow other files than images on richtext editor
CKEDITOR_CONFIGS = {
    'default':{
        # 'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic':[
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig':[
            {'name':'document', 'items':['-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name':'clipboard', 'items':['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {
                'name':'basicstyles',
                'items':['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']
            },
            {'name':'editing', 'items':['Find', 'Replace', '-', 'SelectAll']},
            '/',
            {'name':'styles', 'items':['Styles', 'Format', 'Font', 'FontSize']},
            {'name':'colors', 'items':['TextColor', 'BGColor']},
            {'name':'about', 'items':['About']},

            '/',
            {
                'name':'paragraph',
                'items':['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                         'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                         'Language']
            },
            {'name':'links', 'items':['Link', 'Unlink', 'Anchor']},
            {
                'name':'insert',
                'items':['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']
            },

            '/',
            {
                'name':'yourcustomtools', 'items':[
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
                'ShowBlocks',
                'Source',
            ]
            },
        ],

        'toolbar':'YourCustomToolbarConfig',  # put selected toolbar config here
        'toolbarGroups':[{
            'name':'document',
            'groups':['mode', 'document', 'doctools']
        }],
        # 'height':291,
        # 'width':'100%',
        # 'filebrowserWindowHeight':725,
        # 'filebrowserWindowWidth':940,
        # 'toolbarCanCollapse':True,
        # 'mathJaxLib':'//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces':4,
        'extraPlugins':','.join(
            [
                'uploadimage',  # the upload image feature
                # your extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
            ]
        ),
    }
}
