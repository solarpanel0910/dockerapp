from flask import Flask, jsonify
import pymysql
import os
import time

app = Flask(__name__)

# データベース接続情報
db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')

def get_db_connection():
    while True:
        try:
            conn = pymysql.connect(
                host=db_host,
                user=db_user,
                password=db_password,
                db=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            return conn
        except pymysql.err.OperationalError:
            print("DB接続に失敗。5秒後に再試行します...")
            time.sleep(5)

# 現在の票数を返すAPI
@app.route('/api/votes', methods=['GET'])
def get_votes():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM menu ORDER BY count DESC")
            result = cursor.fetchall()
            return jsonify(result)
    finally:
        conn.close()

# 投票を処理するAPI
@app.route('/api/vote/<int:menu_id>', methods=['POST'])
def add_vote(menu_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE menu SET count = count + 1 WHERE id = %s"
            cursor.execute(sql, (menu_id,))
        conn.commit()
        return jsonify({'status': 'success'})
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)