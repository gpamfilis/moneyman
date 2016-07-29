import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cheese cake'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MONEYMAN_MAIL_SUBJECT_PREFIX = '[MONEYMAN]'
    MONEYMAN_MAIL_SENDER = 'MONEYMAN admin <moneyman@example.com>'
    MONEYMAN_ADMIN = 'GEORGE PAMFILIS' # os.environ.get('MONEYMAN_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'username' # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'password' # os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/dev.db' # os.environ.get('SQLALCHEMY_DATABASE_URI')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/testing.db'  # os.environ.get('SQLALCHEMY_DATABASE_URI')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/production.db'  # os.environ.get('SQLALCHEMY_DATABASE_URI')

config = {
            'development': DevelopmentConfig,
            'testing': TestingConfig,
            'production': ProductionConfig,
            'default': DevelopmentConfig
        }
