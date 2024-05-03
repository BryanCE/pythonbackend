from flask import Blueprint, jsonify
import psycopg2
from db.connect_db import *

#get connection from connect_db.py
conn = connect()

# Create a cursor object
cur = conn.cursor()

# Create a new Blueprint object
products_blueprint = Blueprint('products', __name__, url_prefix='/products')

# API endpoint to get all products
@products_blueprint.route('/', methods=['GET'])
def get_products():
    try:
        cur.execute("SELECT * FROM products;")
        products = cur.fetchall()
        return jsonify([{'id': product[0], 'name': products[1], 'price': products[2]} for product in products])
    except (Exception, psycopg2.Error) as error:
        print("Error executing SQL query:", error)
        return jsonify({'error': str(error)}), 500