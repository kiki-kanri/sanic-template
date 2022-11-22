import sanic_cookiesession

from pathlib import Path
from sanic import Blueprint, Request, Sanic

from library.utils import import_attribute


ROOT = Path(__file__).resolve().parent.parent


def install_apps(sanic_app: Sanic):
    for app_name in sanic_app.config.get('INSTALLED_APPS'):
        bps: list[Blueprint] = import_attribute(
            f'apps.{app_name}.blueprints'
        )

        for bp in bps:
            url_prefix = '/api'

            if bp.url_prefix:
                url_prefix += bp.url_prefix

            sanic_app.blueprint(bp, url_prefix=url_prefix)


def create_app():
    sanic_app = Sanic('SanicApp')
    sanic_app.update_config(ROOT / 'instance' / 'config.py')
    sanic_cookiesession.setup(sanic_app)

    install_apps(sanic_app)

    return sanic_app
