from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

from uberstive.mod_data_retrieving import views
