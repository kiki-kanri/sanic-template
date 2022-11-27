import sanic_cookiesession

from mongoengine import connect
from pathlib import Path
from sanic import Blueprint, Sanic

from library.utils import import_attribute
from .settings import ROOT


def connect_db(sanic_app: Sanic):
    connect(**sanic_app.config['DATABASES']['default'])


def install_apps(sanic_app: Sanic):
    # App blueprints
    for app_name in sanic_app.config['INSTALLED_APPS']:
        bps: list[Blueprint] = import_attribute(
            f'apps.{app_name}.blueprints'
        )

        for bp in bps:
            url_prefix = '/api'

            if bp.url_prefix:
                url_prefix += bp.url_prefix

            sanic_app.blueprint(bp, url_prefix=url_prefix)

    # Middlewares
    for middleware_path in sanic_app.config['MIDDLEWARES']:
        middleware = import_attribute(middleware_path)

        if rq_func := getattr(middleware, 'request', None):
            sanic_app.on_request(rq_func)

        if rp_func := getattr(middleware, 'response', None):
            sanic_app.on_response(rp_func)


def create_app():
    sanic_app = Sanic('SanicApp')
    sanic_app.update_config(ROOT / 'instance/config.py')
    sanic_app.update_config(ROOT / 'main/settings.py')
    sanic_cookiesession.setup(sanic_app)

    connect_db(sanic_app)
    install_apps(sanic_app)

    return sanic_app
