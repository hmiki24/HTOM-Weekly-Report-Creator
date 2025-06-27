# HTOM Weekly Report Creator

HTOM業務で作成する週次レポートを自動生成する Python スクリプトです。

## 🔧 利用方法
1. このリポジトリをクローンし、必要な token(client_id, client_secret,　appkey)を挿入
2. excelファイルに今までのやり取りをコピペで打ち込む

3. 仮想環境の作成と有効化・必要パッケージのインストール
       python3 -m venv path/to/venv
       source path/to/venv/bin/activate
       python3 -m pip install requests
5. 実行
       python3 api_script.py
