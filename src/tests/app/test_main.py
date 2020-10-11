from flask import Flask

app = Flask(__name__)


def test_home_get(client):
    response = client.get('/')
    assert response.status_code == 200


def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)
