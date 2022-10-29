import pytest
from flask.testing import FlaskClient
import os, sys
from flask_babel import Babel, gettext, _
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from server import app


@pytest.fixture
def client():
    babel = Babel(app)
    return app.test_client()


def test_run(client: FlaskClient):
    """should be a successful GET request"""
    resp = client.get('/')
    assert resp.status_code == 200

