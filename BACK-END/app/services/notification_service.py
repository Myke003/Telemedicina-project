from app import mysql
from datetime import datetime

def send_notification(user_id, notification_type, message):
    cursor = mysql.connection.cursor()
    cursor.execute('''
        INSERT INTO notifications (user_id, type, message, status)
        VALUES (%s, %s, %s, %s)
    ''', (user_id, notification_type, message, 'unread'))
    mysql.connection.commit()
    cursor.close()
