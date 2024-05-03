import psycopg2
from db.connect_db import *
from flask import Flask, Blueprint, jsonify, request
from api.users import *
from api.products import *


# Create a Flask app
app = Flask(__name__)
app.register_blueprint(users_blueprint, url_prefix='/api/v1')
app.register_blueprint(products_blueprint, url_prefix='/api/v1')


# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)