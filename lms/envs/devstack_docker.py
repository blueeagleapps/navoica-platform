""" Overrides for Docker-based devstack. """

from .devstack import *  # pylint: disable=wildcard-import, unused-wildcard-import

# Docker does not support the syslog socket at /dev/log. Rely on the console.
LOGGING['handlers']['local'] = LOGGING['handlers']['tracking'] = {
    'class': 'logging.NullHandler',
}

LOGGING['loggers']['tracking']['handlers'] = ['console']
HOMEPAGE_COURSE_MAX = 4

LMS_BASE = os.environ.get('LMS_BASE', '10.10.32.151:18000')
CMS_BASE = os.environ.get('CMS_BASE', '10.10.32.151:18010')

SITE_NAME = LMS_BASE
LMS_ROOT_URL = 'http://{}'.format(LMS_BASE)
LMS_INTERNAL_ROOT_URL = LMS_ROOT_URL

ECOMMERCE_PUBLIC_URL_ROOT = 'http://localhost:18130'
ECOMMERCE_API_URL = 'http://%s:18130/api/v2' % LMS_BASE

#COMMENTS_SERVICE_URL = 'http://edx-dev.opi.org.pl:4567'

ENTERPRISE_API_URL = '{}/enterprise/api/v1/'.format(LMS_INTERNAL_ROOT_URL)

CREDENTIALS_INTERNAL_SERVICE_URL = 'http://%s:18150' % LMS_BASE
CREDENTIALS_PUBLIC_SERVICE_URL = 'http://localhost:18150'

OAUTH_OIDC_ISSUER = '{}/oauth2'.format(LMS_ROOT_URL)
TIME_ZONE = 'Europe/Warsaw'
JWT_AUTH.update({
    'JWT_SECRET_KEY': 'lms-secret',
    'JWT_ISSUER': OAUTH_OIDC_ISSUER,
    'JWT_AUDIENCE': 'lms-key',
})

FEATURES.update({
    'AUTOMATIC_AUTH_FOR_TESTING': True,
    'ENABLE_COURSEWARE_SEARCH': True,
    'ENABLE_COURSE_DISCOVERY': True,
    'ENABLE_DASHBOARD_SEARCH': False,
    'ENABLE_DISCUSSION_SERVICE': True,
    'SHOW_HEADER_LANGUAGE_SELECTOR': True,
    'ENABLE_ENTERPRISE_INTEGRATION': False,
})

ENABLE_MKTG_SITE = os.environ.get('ENABLE_MARKETING_SITE', False)
MARKETING_SITE_ROOT = os.environ.get('MARKETING_SITE_ROOT', 'http://localhost:8080')

MKTG_URLS = {
    'ABOUT': '/about',
    'ACCESSIBILITY': '/accessibility',
    'AFFILIATES': '/affiliate-program',
    'BLOG': '/blog',
    'CAREERS': '/careers',
    'CONTACT': '/support/contact_us',
    'COURSES': '/course',
    'DONATE': '/donate',
    'ENTERPRISE': '/enterprise',
    'FAQ': '/student-faq',
    'HONOR': '/edx-terms-service',
    'HOW_IT_WORKS': '/how-it-works',
    'MEDIA_KIT': '/media-kit',
    'NEWS': '/news-announcements',
    'PRESS': '/press',
    'PRIVACY': '/edx-privacy-policy',
    'ROOT': MARKETING_SITE_ROOT,
    'SCHOOLS': '/schools-partners',
    'SITE_MAP': '/sitemap',
    'TRADEMARKS': '/trademarks',
    'TOS': '/edx-terms-service',
    'TOS_AND_HONOR': '/edx-terms-service',
    'WHAT_IS_VERIFIED_CERT': '/verified-certificate',
}

CREDENTIALS_SERVICE_USERNAME = 'credentials_worker'

COURSE_CATALOG_API_URL = 'http://edx.devstack.discovery:18381/api/v1/'

LANGUAGE_CODE = 'pl'

DEFAULT_FROM_EMAIL = 'registration@'+LMS_BASE
DEFAULT_FEEDBACK_EMAIL = 'feedback@'+LMS_BASE
SERVER_EMAIL = 'devops@'+LMS_BASE


########################## THEMING  #######################
# If you want to enable theming in devstack, uncomment this section and add any relevant
# theme directories to COMPREHENSIVE_THEME_DIRS

# We have to import the private method here because production.py calls
# derive_settings('lms.envs.production') which runs _make_mako_template_dirs with
# the settings from production, which doesn't include these theming settings. Thus,
# the templating engine is unable to find the themed templates because they don't exist
# in it's path. Re-calling derive_settings doesn't work because the settings was already
# changed from a function to a list, and it can't be derived again.

from .common import _make_mako_template_dirs

SITE_ID = 1
# dir containing all themes
COMPREHENSIVE_THEME_DIRS = [REPO_ROOT / "themes"]
# Theme directory locale paths
COMPREHENSIVE_THEME_LOCALE_PATHS = []
# Theme to use when no site or site theme is defined,
# set to None if you want to use openedx theme
DEFAULT_SITE_THEME = 'navoica-theme'

ENABLE_COMPREHENSIVE_THEMING = True

TEMPLATES[1]["DIRS"] = _make_mako_template_dirs
derive_settings(__name__)
