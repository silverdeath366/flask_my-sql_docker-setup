from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

# DB connection config from environment variables
MYSQL_HOST = 'db'
MYSQL_USER = os.getenv('MYSQL_USER', 'flaskuser')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'flaskpass123')
MYSQL_DB = os.getenv('MYSQL_DATABASE', 'flaskdb')

def get_db_connection():
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def home():
    return '🎉 Flask is running and connected to MySQL!'

@app.route('/users')
def list_users():
    conn = None  # ✅ define it first
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
