
from pyramid.config import Configurator

from src.scripts.init import init_db


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('.configure.logging')
    config.include('.auth')
    config.include('.api')

    config.scan(ignore=[])

    init_db('src/database/master.sqlite3')

    return config.make_wsgi_app()
