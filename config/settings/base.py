"""
Django base settings for portfolio project.
"""

import os
from pathlib import Path
import environ

from django.conf import settings

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
PRE_THIRD_PARTY_APPS = [  # Apps to be executed before django contrib apps
    'filebrowser',
]
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
    # CMS - TinyMCE
    'tinymce',
]
LOCAL_APPS = [
    'apps.website.apps.WebsiteConfig'
]

INSTALLED_APPS = PRE_THIRD_PARTY_APPS + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

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
LANGUAGE_CODE = 'en'
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

# Filebrowser
# ---------------------------------------------------------------------------
# Used by TinyMCE to upload files
EXTENSIONS = getattr(settings, "FILEBROWSER_EXTENSIONS", {
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
})
SELECT_FORMATS = getattr(settings, "FILEBROWSER_SELECT_FORMATS", {
    'image': ['Image'],
})
VERSIONS_BASEDIR = getattr(settings, 'FILEBROWSER_VERSIONS_BASEDIR', '_versions')
MAX_UPLOAD_SIZE = getattr(settings, "FILEBROWSER_MAX_UPLOAD_SIZE", 1485760)
NORMALIZE_FILENAME = getattr(settings, "FILEBROWSER_NORMALIZE_FILENAME", True)
CONVERT_FILENAME = getattr(settings, "FILEBROWSER_CONVERT_FILENAME", True)
LIST_PER_PAGE = getattr(settings, "FILEBROWSER_LIST_PER_PAGE", 10)
DEFAULT_SORTING_BY = getattr(settings, "FILEBROWSER_DEFAULT_SORTING_BY", "date")
DEFAULT_SORTING_ORDER = getattr(settings, "FILEBROWSER_DEFAULT_SORTING_ORDER", "desc")

# TinyMCE
# ---------------------------------------------------------------------------
TINYMCE_JS_URL = os.path.join(STATIC_URL, 'js/tinymce_v6/tinymce.min.js')
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, 'js/tinymce_v6')
TINYMCE_DEFAULT_CONFIG = {
    # * Base config
    # ! CSS selector for the html textarea generated by tinymce package -> REQUIRED ON tinyMCE v6
    'selector':'textarea.tinymce',
    'height':'600px',
    'width':'100%',
    'custom_undo_redo_levels':50,

    # * Plugins
    # https://www.tiny.cloud/docs/tinymce/6/plugins/
    'plugins':'advlist autolink anchor autosave charmap code emoticons fullscreen help image insertdatetime link '
              'lists  media nonbreaking pagebreak preview quickbars save searchreplace table visualblocks visualchars '
              'wordcount',
    # Other plugins
    # 'codesample' Need prism.js - https://www.tiny.cloud/docs/tinymce/6/codesample/
    # 'template' - https://www.tiny.cloud/docs/tinymce/6/template/
    # * Plugin configs
    'emoticons_database':'emojis',

    # * Menubar
    'menubar':'file edit view insert format tools table help',

    # * Toolbars
    'toolbar1':'undo redo | fullscreen  preview  print save | searchreplace | charmap emoticons | '
               'hr image media insertdatetime link anchor | visualblocks visualchars code ',
    'toolbar2':'fontfamily fontsize blocks',
    'toolbar3':'bold italic underline strikethrough | '
               'alignleft aligncenter alignright alignjustify | outdent indent | numlist bullist | '
               'forecolor backcolor removeformat',

    # * Quickbars
    'quickbars_selection_toolbar':'bold italic | forecolor h1 h2 h3 | quicklink blockquote',
    'quickbars_insert_toolbar':'false',  # Ex: 'quickimage quicktable | hr pagebreak',
    'quickbars_image_toolbar':'alignleft aligncenter alignright | rotateleft rotateright | imageoptions',
}
