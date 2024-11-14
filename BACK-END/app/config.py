# app/config.py

class Config:
    #SECRET_KEY
    SECRET_KEY = 'secret_key'

    # Configuración de CORS
    CORS_ORIGINS = ['*  ']
    
    # Configuración de la base de datos (MariaDB)
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'telemed'
    MYSQL_PASSWORD = 'telemed'
    MYSQL_DB = 'telemed_db'
