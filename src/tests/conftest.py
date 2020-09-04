import pytest
from app.main import app


# http://flask.pocoo.org/docs/1.1.x/testing/
@pytest.fixture
def main_app():
    app.config['TESTING'] = True
    yield app


@pytest.fixture
def client(main_app):
    return main_app.test_client()


@pytest.fixture()
def create_valid_greeting_request():
    """
    Helper function for creating a correctly-structured
    json request
    """
    def _create_valid_greeting_request(greetee="fixture"):
        return {
            "greetee": greetee
        }
    return _create_valid_greeting_request
