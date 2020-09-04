from flask import Flask

app = Flask(__name__)


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200


def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)


# def test_messages(client):
#     """Test that messages work."""

#     login(client, main.app.config['USERNAME'], main.app.config['PASSWORD'])
#     rv = client.post('/add', data=dict(
#         title='<Hello>',
#         text='<strong>HTML</strong> allowed here'
#     ), follow_redirects=True)
#     assert b'No entries here so far' not in rv.data
#     assert b'&lt;Hello&gt;' in rv.data
#     assert b'<strong>HTML</strong> allowed here' in rv.data


# http://flask.pocoo.org/docs/1.0/testing/#testing-json-apis
def test_hello_greets_greetee(client):
    request_payload = {"greetee": "world"}
    response = client.post("/hello", json=request_payload)
    result = response.get_json()

    assert response.status_code == 200
    assert result is not None
    assert "message" in result
    assert result['message'] == "hello world"


def test_hello_requires_greetee(client):
    request_payload = {}
    response = client.post("/hello", json=request_payload)
    result = response.get_json()

    assert response.status_code == 400
    assert result is not None
    assert "message" in result
    assert "is a required property" in result['message'][0]
