from rauth import OAuth2Service
import os
import requests

UBER_API_URL = 'https://sandbox-api.uber.com/v1.2/'


def login():
    uber_api = OAuth2Service(
        client_id=os.environ['CLIENT_ID'],
        client_secret=os.environ['CLIENT_SECRET'],
        name='stive',
        authorize_url='https://login.uber.com/oauth/authorize',
        access_token_url='https://login.uber.com/oauth/token',
        base_url=UBER_API_URL,
    )
    parameters = {
        'response_type': 'code',
        'redirect_uri': 'http://localhost:5000/oauth/token',
        'scope': 'history',
    }
    login_url = uber_api.get_authorize_url(**parameters)
    return login_url


def access_token(code):
    parameters = {
        'redirect_uri': 'http://localhost:5000/oauth/token',
        'code': code,
        'grant_type': 'authorization_code'
    }

    response = requests.post(
        'https://login.uber.com/oauth/token',
        auth=(
            os.environ['CLIENT_ID'],
            os.environ['CLIENT_SECRET'],
        ),
        data=parameters,
    )
    return response.json().get('access_token')


def history(access_token):
    response = requests.get(
        UBER_API_URL + 'history',
        headers={
            'Authorization': 'Bearer %s' % access_token,
        },
        params={'limit': '50'}  # TODO: improve this logic here to get all the history
    )
    history = response.json()
    requests_id_history = [ride['request_id'] for ride in history['history'] if ride['status'] == 'completed']

    return requests_id_history



