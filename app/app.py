# フラスク（Flask）という、ウェブサイトを作るための道具を読み込みます
from flask import Flask
# JSON（ジェイソン）という、データをやり取りする形式にするための道具を読み込みます
from flask import jsonify
# MySQL（マイエスキューエル）というデータベースを操作するための道具を読み込みます
import pymysql
# パソコン（OS）の設定を確認するための道具を読み込みます
import os

# サーバーの本体を作って、変数「app」に入れます
app = Flask(__name__)

# データベースに接続するための情報を、設定（環境変数）から取り出します
# 住所（DB_HOST）を変数「database_address」に入れます
database_address = os.environ.get('DB_HOST')
# ユーザー名（DB_USER）を変数「user_name」に入れます
user_name = os.environ.get('DB_USER')
# パスワード（DB_PASSWORD）を変数「password」に入れます
password = os.environ.get('DB_PASSWORD')
# データベースの名前（DB_NAME）を変数「database_name」に入れます
database_name = os.environ.get('DB_NAME')

# データベースに接続するための「関数（命令のセット）」を作ります
def get_db_connection():
    # データベースに接続し、その情報を変数「connection」に入れます
    connection = pymysql.connect(
        host=database_address,
        user=user_name,
        password=password,
        db=database_name,
        # データを「キーと値」の分かりやすい形（辞書形式）で受け取る設定にします
        cursorclass=pymysql.cursors.DictCursor
    )
    # 接続した情報を返します
    return connection

# ブラウザから「/api/votes」というURLにリクエストが来た時の処理です
@app.route('/api/votes', methods=['GET'])
def get_votes():
    # データベースに接続します
    db_conn = get_db_connection()
    # データベースに命令を送るための「窓口（カーソル）」を作ります
    db_cursor = db_conn.cursor()
    
    # 実行したい命令（SQL）を変数「sql_command」に入れます
    # 「メニューを、得票数（count）が多い順に全部持ってきて」という命令です
    sql_command = "SELECT * FROM menu ORDER BY count DESC"
    
    # 命令を実行します
    db_cursor.execute(sql_command)
    
    # 命令の結果（すべてのデータ）を受け取って、変数「result_data」に入れます
    result_data = db_cursor.fetchall()
    
    # 窓口（カーソル）を閉じます
    db_cursor.close()
    # データベースとの接続を閉じます
    db_conn.close()
    
    # 受け取ったデータを、ブラウザが分かりやすい形式（JSON）にして返します
    return jsonify(result_data)

# ブラウザから「/api/vote/数字」というURLに投票のリクエストが来た時の処理です
@app.route('/api/vote/<int:menu_id>', methods=['POST'])
def add_vote(menu_id):
    # データベースに接続します
    db_conn = get_db_connection()
    # データベースに命令を送るための「窓口（カーソル）」を作ります
    db_cursor = db_conn.cursor()
    
    # 「指定された番号（id）の投票数を1増やす」という命令を変数「sql_update」に入れます
    sql_update = "UPDATE menu SET count = count + 1 WHERE id = %s"
    
    # 命令を実行します。%s の部分に、投票されたメニューの番号が入ります
    db_cursor.execute(sql_update, (menu_id,))
    
    # データベースの変更を確定（保存）します
    db_conn.commit()
    
    # 窓口（カーソル）を閉じます
    db_cursor.close()
    # データベースとの接続を閉じます
    db_conn.close()
    
    # 成功したことを伝えるメッセージを返します
    return jsonify({'status': 'success'})

# このプログラムが直接実行された場合に、サーバーを動かします
if __name__ == '__main__':
    # 誰からのアクセスも受け付ける（0.0.0.0）設定で、5000番の扉を開いて待ち受けます
    app.run(host='0.0.0.0', port=5000)
