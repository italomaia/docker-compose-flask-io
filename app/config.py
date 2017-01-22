import os
import logging
from datetime import timedelta


# use DEBUG mode?
DEBUG = os.getenv("FLASK_DEBUG") == '1'

# use TESTING mode?
TESTING = os.getenv("FLASK_TEST") == '1'

# use server x-sendfile?
USE_X_SENDFILE = os.getenv("FLASK_USE_X_SENDFILE") == '1'

# DATABASE CONFIGURATION
# see http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#database-urls
SQLALCHEMY_DATABASE_URI = (''.join([
    "postgresql+psycopg2://",
    "{user}:{passwd}@{host}:{port}/{db}"
])).format(
    user=os.environ['POSTGRES_USER'],
    passwd=os.environ['POSTGRES_PASSWORD'],
    host=os.environ['POSTGRES_HOST'],
    port=os.environ['POSTGRES_PORT'],
    db=os.environ['POSTGRES_DB'],
)

# DEBUG mode only!
SQLALCHEMY_ECHO = DEBUG
SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG

WTF_CSRF_ENABLED = not TESTING

# DO NOT LEAVE DEFAULT VALUE FOR PRODUCTION
# generate secret with: import os; os.urandom(24)
SECRET_KEY = os.getenv("FLASK_SECRET", "secret")

# LOGGING
LOGGER_NAME = "app_log"
LOG_LEVEL = logging.INFO
# used by logging.Formatter
LOG_FORMAT = "%(asctime)s %(levelname)s\t: %(message)s"

PERMANENT_SESSION_LIFETIME = timedelta(days=7)

# EMAIL CONFIGURATION
MAIL_SERVER = "localhost"
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_DEBUG = False
MAIL_USERNAME = None
MAIL_PASSWORD = None
DEFAULT_MAIL_SENDER = "do-not-answer@" + os.environ["SERVER_NAME"]

LOAD_MODULES_EXTENSIONS = ['views', 'models']

# only these extensions will be initialized
EXTENSIONS = [
    'extensions.db',
    'extensions.migrate',
    'extensions.glue',
    'extensions.ma',
    'extensions.io',
]

# see example/ for reference
# ex: BLUEPRINTS = ['blog']  # where `blog` is a Blueprint instance
# ex: BLUEPRINTS = [('blog', {'url_prefix': '/myblog'})]  # where `blog` is a Blueprint instance
BLUEPRINTS = []
