from pyramid.config import Configurator
from configparser import ConfigParser # This will be different in Python 2.7
from functools import partial 
import os


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()


def zappa(config_uri, event, context, **vars):
    """
    Uses the settings in the configuration uri to bootstrap a wsgi application
    through pyramid. 

    Zappa then uses that wsgi application
    to create a handler function for use with aws lambda. 

    Event and context information are passed to the handler function which uses
    our wsgi application to return a response.

    :param config_uri: string pointing to paste deploy config file
    :param event: aws event
    :param context: aws context
    :param vars: parameters that will be passed to the configuration file
    :return: response
    """
    config = ConfigParser()
    config.read(config_uri)
    settings = dict(config.items('app:main', vars=vars))
    wsgi_app = main(None, **settings)

    return wsgi_app(event, context)


# the following functions will have a signature similar to: 
# function(event, context)
# which is what zappa seems to like
zappa_dev = partial(zappa,
                    'development.ini'
                    )

zappa_prod = partial(zappa,
                     'production.ini'
                     )
