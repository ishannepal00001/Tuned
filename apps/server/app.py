from flask import Flask

from apps.server.api import api
from pakcages.core.settings import settings


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(api)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(host=settings.host, port=settings.port, debug=settings.debug)
