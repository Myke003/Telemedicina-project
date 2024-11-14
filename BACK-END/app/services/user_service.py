from werkzeug.security import generate_password_hash, check_password_hash
from app.database.db import mysql
import datetime

def get_all_users():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT id, email, name, role, created_at, updated_at FROM users')
    users = cursor.fetchall()
    cursor.close()
    return users

def get_user_by_id(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT id, email, name, role, created_at, updated_at FROM users WHERE id = %s', (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return user

def create_new_user(data):
    hashed_password = generate_password_hash(data['password'])
    cursor = mysql.connection.cursor()
    cursor.execute('''
        INSERT INTO users (email, password, name, role) 
        VALUES (%s, %s, %s, %s)
    ''', (data['email'], hashed_password, data.get('name'), data.get('role', 'patient')))
    mysql.connection.commit()
    new_user_id = cursor.lastrowid
    cursor.close()
    return new_user_id

def update_user_by_id(user_id, data):
    update_fields = []
    update_values = []
    if 'name' in data:
        update_fields.append('name = %s')
        update_values.append(data['name'])
    if 'role' in data:
        update_fields.append('role = %s')
        update_values.append(data['role'])
    if 'password' in data:
        update_fields.append('password = %s')
        update_values.append(generate_password_hash(data['password']))
    if update_fields:
        update_values.append(user_id)
        cursor = mysql.connection.cursor()
        cursor.execute(f'''UPDATE users SET {', '.join(update_fields)} WHERE id = %s''', tuple(update_values))
        mysql.connection.commit()
        cursor.close()
        return cursor.rowcount > 0
    return False

def delete_user_by_id(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
    mysql.connection.commit()
    affected_rows = cursor.rowcount
    cursor.close()
    return affected_rows > 0
