import config
from main import app_factory

# flask-io is already initialized
app = app_factory(config, 'app')
