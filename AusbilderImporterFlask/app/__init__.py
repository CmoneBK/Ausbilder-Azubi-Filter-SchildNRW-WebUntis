from flask import Flask
from flask_caching import Cache
import logging
import os

print("Initializing the application...")

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Setup Logging
log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.log')
logging.basicConfig(filename=log_path, level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

# Additionally, output to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# Import routes at the end to avoid circular imports
from app import routes

print("Application initialized.")

# Explicitly export app
__all__ = ['app']
