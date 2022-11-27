from pathlib import Path


AUTO_EXTEND = False

FALLBACK_ERROR_FORMAT = 'json'

# App dir name
INSTALLED_APPS = [
    'example'
]

# Middleware class import path
MIDDLEWARES = [
    'apps.example.middlewares.example.ExampleMiddleware'
]

NOISY_EXCEPTIONS = True
ROOT = Path(__file__).resolve().parent.parent
