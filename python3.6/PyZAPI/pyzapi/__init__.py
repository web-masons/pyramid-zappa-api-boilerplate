from pyramid.config import Configurator
import pyzapi.app

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    return app.main(global_config, **settings)
