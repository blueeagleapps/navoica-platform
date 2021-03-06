""" Overrides for Docker-based devstack. """

from .devstack import *  # pylint: disable=wildcard-import, unused-wildcard-import

# Docker does not support the syslog socket at /dev/log. Rely on the console.
LOGGING['handlers']['local'] = LOGGING['handlers']['tracking'] = {
    'class': 'logging.NullHandler',
}

LOGGING['loggers']['tracking']['handlers'] = ['console']

PLATFORM_NAME = 'Studio Navoica Draft'
LMS_BASE = 'draft.navoica.pl'
CMS_BASE = 'studio-draft.navoica.pl'
LMS_ROOT_URL = 'http://{}'.format(LMS_BASE)

FEATURES.update({
    'ENABLE_COURSEWARE_INDEX': True,
    'ENABLE_LIBRARY_INDEX': True,
    'ENABLE_DISCUSSION_SERVICE': True,
    'ENABLE_VIDEO_UPLOAD_PIPELINE': True,
    "PREVIEW_LMS_BASE": "preview-draft.navoica.pl",
})

CREDENTIALS_SERVICE_USERNAME = 'credentials_worker'

OAUTH_OIDC_ISSUER = '{}/oauth2'.format(LMS_ROOT_URL)

JWT_AUTH.update({
    'JWT_SECRET_KEY': 'lms-secret',
    'JWT_ISSUER': OAUTH_OIDC_ISSUER,
    'JWT_AUDIENCE': 'lms-key',
})
TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'pl'



DEFAULT_FROM_EMAIL = 'registration@draft.navoica.pl'
DEFAULT_FEEDBACK_EMAIL = 'feedback@draft.navoica.pl'
SERVER_EMAIL = 'devops@draft.navoica.pl'

WEBPACK_CONFIG_PATH = 'webpack.prod.config.js'

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'lms.envs.draft.should_show_debug_toolbar',
}

def should_show_debug_toolbar(request):
    return False
