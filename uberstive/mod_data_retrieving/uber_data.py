# -*- coding: utf-8 -*-

from flask import render_template, redirect, request
from uberstive import app
from rauth import OAuth2Service
import requests


@app.route('/', methods=['GET'])
def history():
    return render_template("home.html", history=user_history())

def user_history():
    # https://api.uber.com/v1.2/history
    # parameters = {'apikey': PUBLIC_KEY, 'ts': timestamp, 'hash': hash_, 'limit': 100, 'offset': n}

    # history = requests.get('http://gateway.marvel.com/v1/public/characters', params=parametros)  # requisica
    return "ana delicia"

@app.route('/oauth/login')
def login():

  uber_api = OAuth2Service(
    client_id='EsBJfHieCNX8wIGVrYCjvB0o-iIZf78Y',
    client_secret='WPrvB3CRxggnHXWqzdGKPbyohJCpkyj7epBAp7FU',
    name='stive',
    authorize_url='https://login.uber.com/oauth/authorize',
    access_token_url='https://login.uber.com/oauth/token',
    base_url='https://sandbox-api.uber.com/v1/'
  )

  parameters = {
    'response_type': 'code',
    'redirect_uri': 'http://localhost:5000/oauth/cb', # your callback url for oauth2 step 2
    'scope': 'profile',
  }

  # Redirect user here to authorize your application
  login_url = uber_api.get_authorize_url(**parameters)
  return redirect(login_url)

@app.route('/oauth/cb')
def test():

  parameters = {
    'redirect_uri': 'http://localhost:8080/oauth/cb',
    'code': request.args.get('code'),
    'grant_type': 'authorization_code',
  }

  response = requests.post(
    'https://login.uber.com/oauth/token',
    auth=(
      'EsBJfHieCNX8wIGVrYCjvB0o-iIZf78Y',
      'WPrvB3CRxggnHXWqzdGKPbyohJCpkyj7epBAp7FU',
    ),
    data=parameters,
  )


  # This access_token is what we'll use to make requests in the following steps
  access_token = response.json().get('access_token')
  print(response)

  return "mateus"
  # access_token = request.args.get('access_token')

  #response = requests.get(
  #  'https://api.uber.com/v1' + '/me',
  #  headers={
  #    'Authorization': 'Bearer %s' % access_token
  #  }
  #)

  #data = response.text
  #return data


  # return access_token

@app.route('/profile')
def profile():

  access_token = request.args.get('access_token')

  response = requests.get(
    'https://api.uber.com/v1' + '/me',
    headers={
        'Authorization': 'Bearer %s' % access_token
    }
  )

  data = response.text
  return data

