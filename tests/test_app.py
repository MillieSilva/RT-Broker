# System Imports

# Application Imports
from broker import app


# Library Imports


def test_client():
    flask_app = app.flask_app

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            return testing_client

