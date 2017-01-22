from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_jsglue import JSGlue
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate(db=db)
io = SocketIO()
glue = JSGlue()
ma = Marshmallow()
