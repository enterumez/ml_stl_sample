# ベースとなるイメージを指定
FROM python:3.10.11-slim-buster

# ディレクトリを作成し、作業用ディレクトリに指定する。
RUN mkdir /opt/app
WORKDIR /opt/app

# requirements.txtをコピーする。
COPY ./requirements.txt /opt/app/requirements.txt

# 環境変数に、アプリケーションのルートディレクトリを設定する。
ENV PYTHONPATH=/opt/app

# ライブラリをインストールする。
RUN pip install --upgrade pip && pip install -r requirements.txt && rm requirements.txt

# コンテナ起動時のコマンドを指定する。
CMD ["streamlit", "run", "./src/app.py"]
