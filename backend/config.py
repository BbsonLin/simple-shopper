import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    SECRET_KEY = 'secret-for-simple-shopper-app'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TEMPLATE_FOLDER = os.path.abspath('./app/templates/')
    STATIC_FOLDER = os.path.abspath('./app/static/')
    EXTRA_DIRS = [TEMPLATE_FOLDER, STATIC_FOLDER]
    ENABLED_MODULES = (
        'product',
        'cart',
        'store',
        'api',
    )


class DevelopmentConfig(BaseConfig):
    TEMPLATE_FOLDER = os.path.abspath('../frontend/dist/')
    STATIC_FOLDER = os.path.abspath('../frontend/dist/static/')
    EXTRA_DIRS = [TEMPLATE_FOLDER, STATIC_FOLDER]
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}