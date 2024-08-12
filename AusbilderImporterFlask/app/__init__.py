from flask import Flask
from flask_caching import Cache
import logging
import os
import configparser

print("Initializing the application...")

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Set a secret key
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Ensure upload folder exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Setup Logging
log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.log')
logging.basicConfig(filename=log_path, level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

# Additionally, output to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# Ensure config.ini exists and is properly formatted
def create_default_ini_file(ini_path):
    config = configparser.ConfigParser()
    config['FILTER'] = {'Classes': ''}
    config['BLACKLIST'] = {'IDs': ''}
    config['CSV'] = {'InputPath': ''}  # Füge die CSV-Sektion hinzu
    with open(ini_path, 'w') as configfile:
        config.write(configfile)

ini_path = os.path.join(os.getcwd(), 'config.ini')
if not os.path.exists(ini_path):
    create_default_ini_file(ini_path)

# Import routes at the end to avoid circular imports
from app import routes

print("Application initialized.")

# Explicitly export app
__all__ = ['app']
