import os
import app
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = '123456790'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MAIL_SERVER = 'smtp.google.com'
MAIL_PORT = 587
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_DEBUG = False
MAIL_USERNAME = 'your@gmail.com'
MAIL_PASSWORD = 'password!!'
DEFAULT_SENDER = 'default@google.com'
