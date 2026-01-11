# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリ
WORKDIR /app

# 必要なライブラリをインストール
RUN pip install flask pymysql

# プログラムをコンテナ内にコピー
COPY app.py .

# コンテナ起動時に実行するコマンド
CMD ["python", "app.py"]