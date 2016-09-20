# Config variables for the application...
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False
THREADS_PER_PAGE = 2
CSRF_ENABLED = True
CSRF_SESSION_KEY = 'AsdaSDeqiiw78!*hajhsd*1*71jsjah@4Asd'
SECRET_KEY = 'AaskdASdmA*1273aSDHasy86123@12ja'

SERVERNAME = '127.0.0.1:8080' # dev
#SERVERNAME = 'http://utldr.co' # pro

DEBUG = True # dev
#DEBUG = False #pro
