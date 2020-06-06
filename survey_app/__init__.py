# survey_app/__init__.py

from flask import Flask

# Initialize the survey_app
app = Flask(__name__, instance_relative_config=True, static_url_path='')
# set secret key
app.config['SECRET_KEY'] = 'superspecialsecretkey'
# Load the config file
app.config.from_object('config')

# Load the routes
from survey_app import routes
