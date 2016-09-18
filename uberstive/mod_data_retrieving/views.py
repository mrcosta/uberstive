from flask import render_template, redirect, request
from uberstive import app
from uberstive.mod_data_retrieving.uber_data import history, login, access_token


@app.route('/teste', methods=['GET'])
def teste():
    return 'teste'


@app.route('/', methods=['GET'])
def visited_places():
    # for now history, and then most visited places
    return history(request.args.get('access_token'))


@app.route('/oauth/login')
def uber_authorization():
    login_url = login()
    return redirect(login_url)


@app.route('/oauth/token')
def uber_access_token():
    return redirect('/?access_token=' + access_token(request.args.get('code')))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404






