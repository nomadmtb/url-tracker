# Config variables for the application...
import os, string, random
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False
THREADS_PER_PAGE = 2
CSRF_ENABLED = True
CSRF_SESSION_KEY = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(50)])
SECRET_KEY = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(50)])

SERVERNAME = 'http://127.0.0.1:8080' if DEBUG else 'https://utldr.co'
RECAPCHA_SECRET = 'XXX' if 'RECAPCHA_SECRET' not in os.environ else os.environ['RECAPCHA_SECRET']
RECAPCHA_KEY = 'XXX' if 'RECAPCHA_KEY' not in os.environ else os.environ['RECAPCHA_KEY']
