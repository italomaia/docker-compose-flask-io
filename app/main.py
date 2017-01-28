from empty import Empty
import sys
import os

# apps is a special folder where you can place your blueprints
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_PATH, "apps"))


def app_factory(config, app_name, blueprints=None):
    app = App(app_name)

    app.configure(config)
    app.add_blueprint_list(blueprints or config.BLUEPRINTS)
    app.setup()

    return app


class App(Empty):
    def configure_views(self):
        @self.route("/")
        def index():
            return "oi"
