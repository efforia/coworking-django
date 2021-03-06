#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import os

######################
# CARTRIDGE SETTINGS #
######################

# The following settings are already defined in cartridge.shop.defaults
# with default values, but are common enough to be put here, commented
# out, for convenient overriding.

# Sequence of available credit card types for payment.
# SHOP_CARD_TYPES = ("Mastercard", "Visa", "Diners", "Amex")

# Setting to turn on featured images for shop categories. Defaults to False.
# SHOP_CATEGORY_USE_FEATURED_IMAGE = True

# Set an alternative OrderForm class for the checkout process.
SHOP_CHECKOUT_FORM_CLASS = 'store.forms.ExternalPaymentOrderForm'

# If True, the checkout process is split into separate
# billing/shipping and payment steps.
SHOP_CHECKOUT_STEPS_SPLIT = True

# If True, the checkout process has a final confirmation step before
# completion.
SHOP_CHECKOUT_STEPS_CONFIRMATION = False

# Controls the formatting of monetary values accord to the locale
# module in the python standard library. If an empty string is
# used, will fall back to the system's locale.
SHOP_CURRENCY_LOCALE = "pt_BR.UTF-8"

# Dotted package path and class name of the function that
# is called on submit of the billing/shipping checkout step. This
# is where shipping calculation can be performed and set using the
# function ``cartridge.shop.utils.set_shipping``.
SHOP_HANDLER_BILLING_SHIPPING = "shipping.hooks.fretefacil_shipping_handler"

# Dotted package path and class name of the function that
# is called once an order is successful and all of the order
# object's data has been created. This is where any custom order
# processing should be implemented.
SHOP_HANDLER_TAX = "cartridge.shop.checkout.default_tax_handler"
SHOP_HANDLER_ORDER = None

# Dotted package path and class name of the function that
# is called on submit of the payment checkout step. This is where
# integration with a payment gateway should be implemented.
SHOP_HANDLER_PAYMENT = "feedly.hooks.multiple_payment_handler"

# Sequence of value/name pairs for order statuses.
# SHOP_ORDER_STATUS_CHOICES = (
#     (1, "Unprocessed"),
#     (2, "Processed"),
# )

# Sequence of value/name pairs for types of product options,
# eg Size, Colour.
# SHOP_OPTION_TYPE_CHOICES = (
#     (1, "Size"),
#     (2, "Colour"),
# )

# Sequence of indexes from the SHOP_OPTION_TYPE_CHOICES setting that
# control how the options should be ordered in the admin,
# eg for "Colour" then "Size" given the above:
# SHOP_OPTION_ADMIN_ORDER = (2, 1)

######################
# MEZZANINE SETTINGS #
######################

# The following settings are already defined with default values in
# the ``defaults.py`` module within each of Mezzanine's apps, but are
# common enough to be put here, commented out, for convenient
# overriding. Please consult the settings documentation for a full list
# of settings Mezzanine implements:
# http://mezzanine.jupo.org/docs/configuration.html#default-settings

# Controls the ordering and grouping of the admin menu.
#
# ADMIN_MENU_ORDER = (
#     ("Content", ("pages.Page", "blog.BlogPost",
#        "generic.ThreadedComment", ("Media Library", "fb_browse"),)),
#     ("Shop", ("shop.Product", "shop.ProductOption", "shop.DiscountCode",
#         "shop.Sale", "shop.Order")),
#     ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
#     ("Users", ("auth.User", "auth.Group",)),
# )

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
#
# DASHBOARD_TAGS = (
#     ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
#     ("comment_tags.recent_comments",),
#     ("mezzanine_tags.recent_actions",),
# )

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

# PAGE_MENU_TEMPLATES = (
#     (1, "Top navigation bar", "pages/menus/dropdown.html"),
#     (2, "Left-hand tree", "pages/menus/tree.html"),
#     (3, "Footer", "pages/menus/footer.html"),
# )

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
EXTRA_MODEL_FIELDS = (
    (
        "cartridge.shop.models.Order.paypal_redirect_token",
        "django.db.models.CharField",
        (),
        {"blank":True,"max_length":36},
    ),
    (
        "cartridge.shop.models.Order.pagseguro_redirect",
        "django.db.models.CharField",
        (),
        {"blank":True,"null":True,"max_length":200},
    ),      
)

# Setting to turn on featured images for blog posts. Defaults to False.
#
# BLOG_USE_FEATURED_IMAGE = True

# If True, the south application will be automatically added to the
# INSTALLED_APPS setting.
USE_SOUTH = True

SITE_TITLE = 'Fábrica de Ideias Coworking'

########################
# APPS DJANGO SETTINGS #
########################

LOCALE_DATE = ('Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dec')
STORE_POSTCODE = '90020110'
STORE_COUNTRY = 'Brasil'

PAYPAL_RECEIVER_EMAIL = 'fabricadeideiascw@gmail.com'

PAYPAL_CLIENT_ID = 'AeiijxAGPGKJ1J94r7u7nqX_8oCKtOzI0ZNChSIMwAkEg2Y3wff8FQhPfGZw'
PAYPAL_CLIENT_SECRET = 'EKmSiRBgd31RKZ324o47--u1IgxoOMI-J6UvuIP-X5qFSm30xYy_ULllqHIc'

PAGSEGURO_EMAIL_COBRANCA = 'fabricadeideiascw@gmail.com'
PAGSEGURO_TOKEN = 'D9BBC61094BB4C8BADB296613350FF20'

SHOP_CURRENCY = 'BRL'

DEFAULT_HOST = 'www.fabricadeideiascw.com.br'

########################
# MAIN DJANGO SETTINGS #
########################

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'contato@fabricadeideiascw.com.br'
EMAIL_HOST_PASSWORD = 'coworking409'

#DEFAULT_FROM_EMAIL = 'contato@efforia.com.br'
#SERVER_EMAIL = 'contato@efforia.com.br'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# People who get code error notifications.
# In the format (('Full Name', 'email@example.com'),
#                ('Full Name', 'anotheremail@example.com'))
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "pt-BR"

# Supported languages
_ = lambda s: s
LANGUAGES = (
    ('pt-BR', _('Brazilian Portuguese')),
)

# A boolean that turns on/off debug mode. When set to ``True``, stack traces
# are displayed for error pages. Should always be set to ``False`` in
# production. Best set to ``True`` in local_settings.py
DEBUG = True

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Tuple of IP addresses, as strings, that:
#   * See debug comments, when DEBUG is true
#   * Receive x-headers
INTERNAL_IPS = ("127.0.0.1",)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

AUTHENTICATION_BACKENDS = (
    "mezzanine.core.auth_backends.MezzanineBackend",
    'django.contrib.auth.backends.ModelBackend',
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    'social_auth.backends.contrib.github.GithubBackend',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# The numeric mode to set newly-uploaded files to. The value should be
# a mode you'd pass directly to os.chmod.
FILE_UPLOAD_PERMISSIONS = 0o644


#############
# DATABASES #
#############

DATABASES = {
    "default": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

###################
# S3 STATIC FILES #
###################

AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = 'AKIAIXTTZYYYQMUBVFFQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'fabricadeideias'
AWS_PRELOAD_METADATA = True #helps collectstatic do updates

###########
# LOGGING #
###########

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
}

#########
# PATHS #
#########

# Full filesystem path to the project.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Name of the directory for the project.
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]

# Every cache key will get prefixed with this value - here we set it to
# the name of the directory the project is in to try and use something
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'public'),
)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/static/media/"

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))

# Package/module name to import the root urlpatterns from for the project.
# ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME
ROOT_URLCONF = "urls"

# Put strings here, like "/home/html/django_templates"
# or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)


################
# APPLICATIONS #
################

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "cartridge.shop",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.pages",
    "mezzanine.galleries",
    "mezzanine.twitter",
    "mezzanine.accounts",
    "social_auth",
    "crispy_forms",
    "pure_pagination",
    "socialize",
    "shipping",
    "feedly",
    "store",
    "storages",
    "south"
)

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "social_auth.context_processors.social_auth_by_type_backends",
    "social_auth.context_processors.social_auth_login_redirect",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "mezzanine.conf.context_processors.settings",
    "mezzanine.pages.context_processors.page"
)

# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "cartridge.shop.middleware.ShopMiddleware",
    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    # Uncomment the following if using any of the SSL settings:
    # "mezzanine.core.middleware.SSLRedirectMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}

###################
# DEPLOY SETTINGS #
###################

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

SECRET_KEY = "928f26e4-2b36-48c1-b9b7-5e2049306018df5334a2-3efa-4de8-a10b-010226b85823eaa7584f-0878-43f2-b099-45f4b73519af"
NEVERCACHE_KEY = "0085b0ee-8947-4699-ba15-6bbf538cf75f06e504a2-ee28-4c9e-8a23-ffa5bdebc69384f3b8c4-e63f-4c95-874f-d43f59ff92aa"
SSH_USER = "azureuser"

FABRIC = {
    "SSH_USER": SSH_USER,  # SSH username
    "SSH_PASS":  "mk28to#$",  # SSH password (consider key-based authentication)
    "SSH_KEY_PATH":  "",  # Local path to SSH key file, for key-based auth
    "HOSTS": ["flyingdutchman.cloudapp.net"],  # List of hosts to deploy to
    "VIRTUALENV_HOME":  "/home/%s" % SSH_USER,  # Absolute remote path for virtualenvs
    "PROJECT_NAME": "fabrica",  # Unique identifier for project
    "REQUIREMENTS_PATH": "requirements.txt",  # Path to pip requirements, relative to project
    "GUNICORN_PORT": 9000,  # Port gunicorn will listen on
    "LOCALE": "pt_BR.UTF-8",  # Should end with ".UTF-8"
    "LIVE_HOSTNAME": "factory.fabricadeideiascw.com.br",  # Host for public site.
    "REPO_URL": "git@factory.fabricadeideiascw.com.br:~/fabrica.git",  # Git or Mercurial remote repo URL for the project
    "DB_PASS": "mk28to#$",  # Live database password
    "ADMIN_PASS": "mk28to#$",  # Live admin user password
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
}

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_efforiaid'
SOCIAL_AUTH_UID_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16

# Preenchimento obrigatorio para cada backend que for utilizado
GITHUB_APP_ID                = '45b9116a0e2152049110'
GITHUB_API_SECRET            = '7bb2f71373d42f517982136eaca9041b58b78a0c'
TWITTER_CONSUMER_KEY         = 'oUa8pDde2HDLnVfT8P8p4g'
TWITTER_CONSUMER_SECRET      = 'viyd4XjO4tJ9RIjK97HVX4FSocYMv3mgjvEt5vBH28Y'
FACEBOOK_APP_ID              = '153246718126522'
FACEBOOK_API_SECRET          = '15f57d59a69b96c3d3013b4c9aa301f2'
GOOGLE_OAUTH2_CLIENT_ID      = '112616016687-tbvt0i5pk7ggmn0dn0uatv55benuvsp5.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'PPf7YJ7S0b3GaOI4UFoIw53t'
FOURSQUARE_CONSUMER_KEY      = 'HRGDML5VAGTUB1D22ICA51L4LXPZRQZI2SQS24X2XOCXRIO2'
FOURSQUARE_CONSUMER_SECRET   = 'VBLTME2BBUAYDJJC1JF4FUAISBPOCOIEBSPWR3IWPVVRXMFL'

SOCIAL_AUTH_PIPELINE = (
        'social_auth.backends.pipeline.social.social_auth_user',
        'social_auth.backends.pipeline.associate.associate_by_email',
        'social_auth.backends.pipeline.misc.save_status_to_session',
        'social_auth.backends.pipeline.user.create_user',
        'social_auth.backends.pipeline.social.associate_user',
        'social_auth.backends.pipeline.social.load_extra_data',
        'social_auth.backends.pipeline.user.update_user_details',
        'social_auth.backends.pipeline.misc.save_status_to_session',
)

LOGIN_URL          = '/accounts/login'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/'

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
ANONYMOUS_USER_ID = -1
# AUTH_PROFILE_MODULE = 'efforia.Profile'

##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.
#try:
from local_settings import *
#except ImportError:
    # Parse database configuration from $DATABASE_URL
#    import dj_database_url
#    DATABASES['default'] = dj_database_url.config()
#    STATICFILES_STORAGE = 's3.S3BotoStorage'
#    DEFAULT_FILE_STORAGE = 's3.S3BotoStorage'
#    STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
#    MEDIA_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
#    ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli'



####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
