import os
import dj_database_url
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP


# Django settings for latech project.
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

AUTH_PROFILE_MODULE ='contacts.Contact'

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Latech Administration',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'companies': 'icon-briefcase',
        'contacts':'icon-user',
        'location':'icon-globe',
        'fileupload':'icon-file',
        'taxonomy':'icon-tag',

    },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU_ORDER': (
    #     ('sites',),
    #     ('auth', ('user','group')),
    # ),

    # misc
    'LIST_PER_PAGE': 15
}

IN_HEROKU = bool(os.environ.get('HEROKU_ENV', ''))


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

if os.getenv('HEROKU_ENV') == 'True':
    DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2',}}
    DATABASES['default'] =  dj_database_url.config()
    GS_BUCKET_NAME=os.environ.get('GS_BUCKET_NAME')
    MEDIA_URL = ('http://commondatastorage.googleapis.com/%s/' % os.environ['GS_BUCKET_NAME'])
    MEDIA_ROOT = ''
    STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
    GS_ACCESS_KEY_ID=os.environ.get('GS_SECRET_KEY_ID')
    GS_SECRET_ACCESS_KEY=os.environ.get('GS_SECRET_ACCESS_KEY')
    DEFAULT_FILE_STORAGE = 'storages.backends.gs.GSBotoStorage'
    DEBUG = False
    
else:

    DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': 'latech.db',}}
    MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
    MEDIA_URL = '/media/'
    STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__), 'static'),)
    DEBUG = True


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#MEDIA_URL = '/media/'

#ADMIN_MEDIA_PREFIX = '/static/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = os.path.join(SITE_ROOT, 'static')


# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
#STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(os.path.dirname(__file__), 'static'),
#)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2$u9frxr6r%tw(ub57$o6q)^z39j37)u4r4!r&amp;w09-74$opjq$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'latech.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'latech.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), 'templates')

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'suit',
    'django.contrib.admin',
    'django.contrib.comments',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'companies',
    'contacts',
#    'registration_defaults',
    'taxonomy',
    'location',
#    'taggit',
    'south',
    'fileupload',
    'storagess',
    'news',
#    'django_boto',    
#    'projects',
#    'urls',

)


ACCOUNT_INVITATION_DAYS = 1
INVITATIONS_PER_USER = 1


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# Parse database configuration from $DATABASE_URL
#DATABASES['default'] =  dj_database_url.config()
