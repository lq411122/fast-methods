import pytest
from app.main import create_app
from starlette.testclient import TestClient


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    # db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    app = create_app()
    # app.mq.run()
    yield app

    # close and remove the temporary database
    # os.close(db_fd)
    # os.unlink(db_path)


@pytest.fixture
def client(app):
    """A test client for the app."""
    client = TestClient(app)
    return client












