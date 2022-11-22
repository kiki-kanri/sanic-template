AUTO_EXTEND = False

DATABASES = {
    'default': {
        'authentication_source': 'admin',
        'db': '',
        'host': '127.0.0.1',
        'password': '',
        'port': 27017,
        'username': ''
    }
}

FALLBACK_ERROR_FORMAT = 'json'

INSTALLED_APPS = [
    'home'
]

NOISY_EXCEPTIONS = True
SESSION_COOKIE_SECRET_KEY = ''
