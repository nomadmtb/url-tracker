import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'AsdaSDeqiiw78!*hajhsd*1*71jsjah@4Asd'
    SECRET_KEY = 'AaskdASdmA*1273aSDHasy86123@12ja'
    SERVER_NAME = '0.0.0.0:8080'

class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True

class ProConfig(BaseConfig):
    SERVER_NAME = 'proserver.pro:80'
