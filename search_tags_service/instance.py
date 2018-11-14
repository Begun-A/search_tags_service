import os

from flask import Flask

from search_tags_service.api.v1.tags.resources import blueprint


def configure_from_default_config(app):
    config_name = os.getenv('ENV', 'development').lower().title()
    app.config.from_object('search_tags_service.config.{}Config'.format(config_name))
    app.logger.info('Config: %s', config_name)


def configure_app(app, config_obj=None):
    """ Flask application instance configuration """
    if config_obj:
        app.config.from_object(config_obj)
    else:
        configure_from_default_config(app)


def init_api(app):
    app.register_blueprint(blueprint)


def create_app(app_name='geo', config_obj=None):
    """ App factory """
    app = Flask(app_name)
    configure_app(app, config_obj=config_obj)
    init_api(app)
    return app


# The application instance to use directly or by Gunicorn
app = create_app()


@app.route('/')
def index():
    return 'Welcome to Search Tags Service API!'


if __name__ == '__main__':
    app.run()
