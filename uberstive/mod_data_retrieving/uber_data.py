from flask import render_template, redirect, request
from uberstive import app
from rauth import OAuth2Service
import requests
import os

UBER_API_URL = 'https://sandbox-api.uber.com/v1/'


@app.route('/', methods=['GET'])
def history():
    return render_template("home.html", history=user_history())


def user_history():
    # https://api.uber.com/v1.2/history
    # parameters = {}
    # history = requests.get(UBER_API_URL + 'history', params=parameters)
    return "ana delicia"


@app.route('/oauth/login')
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
        'redirect_uri': 'http://localhost:5000/oauth/cb',
        'scope': 'profile',
    }

    login_url = uber_api.get_authorize_url(**parameters)
    return redirect(login_url)


@app.route('/oauth/cb')
def get_access_token():
    parameters = {
        'redirect_uri': 'http://localhost:5000/oauth/cb',
        'code': request.args.get('code'),
        'grant_type': 'authorization_code',
    }

    response = requests.post(
        'https://login.uber.com/oauth/token',
        auth=(
            os.environ['CLIENT_ID'],
            os.environ['CLIENT_SECRET'],
        ),
        data=parameters,
    )

    access_token = response.json().get('access_token')
    return access_token


@app.route('/profile')
def profile():
    access_token = request.args.get('access_token')

    response = requests.get(
        UBER_API_URL + 'me',
        headers={
            'Authorization': 'Bearer %s' % access_token
        }
    )

    data = response.text
    return data
