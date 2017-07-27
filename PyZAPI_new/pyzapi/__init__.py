from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models.meta import (
    DBSession,
    Base,
    )

from .util.jsonhelpers import custom_json_renderer
from .util.jsonhelpers2 import custom_json_renderer2

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_renderer('json', custom_json_renderer())
    config.add_renderer('json2', custom_json_renderer2())

    config.include('.models')
    config.include('.routes')

    config.scan()
    return config.make_wsgi_app()
