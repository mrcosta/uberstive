from flask import render_template, redirect, request
from uberstive import app
from rauth import OAuth2Service
import requests
import os

UBER_API_URL = 'https://sandbox-api.uber.com/v1.2/'


@app.route('/', methods=['GET'])
def history():
    return render_template("home.html", history=user_history())

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
        'redirect_uri': 'http://localhost:5000/oauth/token',
        'scope': 'history',
    }

    login_url = uber_api.get_authorize_url(**parameters)
    return redirect(login_url)


@app.route('/oauth/token')
def get_access_token():
    parameters = {
        'redirect_uri': 'http://localhost:5000/oauth/token',
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
    return redirect('profile?access_token=' + access_token)


@app.route('/profile')
def profile():
    access_token = request.args.get('access_token')

    response = requests.get(
        UBER_API_URL + 'history',
        headers={
            'Authorization': 'Bearer %s' % access_token,
        },
        params={'limit': '50'} #TODO: improve this logic here to get all the history
    )

    data = response.text
    return data
