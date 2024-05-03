from flask import Blueprint, jsonify, request
import psycopg2
from db.connect_db import *

#get connection from connect_db.py
conn = connect()

# Create a cursor object
cur = conn.cursor()

# Create a new Blueprint object
users_blueprint = Blueprint('users', __name__)

# API endpoint to get all users
@users_blueprint.route('/users', methods=['GET'])
def get_users():
    try:
        cur.execute("SELECT * FROM users;")
        users = cur.fetchall()
        return jsonify([{'id': user[0], 'name': user[1], 'email': user[2]} for user in users])
    except (Exception, psycopg2.Error) as error:
        print("Error executing SQL query:", error)
        return jsonify({'error': str(error)}), 500
    
    # API endpoint to get a user by name
@users_blueprint.route('/user/<name>', methods=['GET'])
def get_user_by_name(name):
    try:
        cur.execute("SELECT * FROM users WHERE name = %s;", (name,))
        user = cur.fetchone()

        if user:
            return jsonify({'id': user[0], 'name': user[1], 'email': user[2]})
        else:
            return jsonify({'message': f'User with name {name} not found'}), 404
    except (Exception, psycopg2.Error) as error:
        print("Error executing SQL query:", error)
        return jsonify({'error': str(error)}), 500
    

    # API endpoint to create a new user
@users_blueprint.route('/user', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({'error': 'Name and email are required'}), 400

        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;", (name, email))
        user_id = cur.fetchone()[0]
        conn.commit()

        return '', 201
    except (Exception, psycopg2.Error) as error:
        print("Error executing SQL query:", error)
        conn.rollback()
        return jsonify({'error': str(error)}), 500