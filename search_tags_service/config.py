from os import getenv


class Config(object):
    DEBUG = False
    HOST = getenv('HOST', '0.0.0.0')
    PORT = getenv('PORT', 80)
    REQUEST_LIFETIME = 30


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = getenv('PORT', 8080)
