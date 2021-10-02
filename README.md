# 目的

ローカル環境で postgres データベースと SQLAlchemy の動作を確認したかったため、作成しました。
サンプルとして、ユーザーテーブルとユーザースコアテーブルを用意し最低限の動きを実装しています。  


# 使用方法

1. Docker の起動
1. Python 仮想環境の起動
1. テストしたいコードの実装

## Docker の起動

1. docker フォルダに移動
1. `docker-compose up -d`コマンドを実行
1. 5432 ポートにて PostgreSQL の環境が立ち上がっていることを確認

## Python 仮想環境の起動

※Windows の場合、PowerShell で権限を通す設定が必要になる場合があります。  
参考: https://qiita.com/enya314/items/0e62b68fe70f52a628bf

1. `python -m venv sql_alchemy_postgres_test_env`を実行
1. `pip install -r requirements.txt`を実行

## テストしたいコードの実装

1. app\test.py に、テストしたいコードを記載。
1. `python test.py`で実行。
1. import のエラーが出る場合、app\database\_\_init\_\_.py に app フォルダへの絶対パスを記載する。