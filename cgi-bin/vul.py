#!/usr/bin/python3

import subprocess
import cgi
import io
import sys

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# POSTされたデータの取得
form = cgi.FieldStorage()
# inputタグのname='string'の入力値を取得
string = form.getvalue('string')
# コマンドの組み立て
cmd = "echo " + str(string) + " | rev"
# subprocessでコマンドの実行
vul = subprocess.run(cmd, shell=True, encoding='utf-8', stdout=subprocess.PIPE)

# レスポンスヘッダの返却
print('Content-type: text/html; charset=UTF-8')
print('')
# レスポンスボディの返却
print(f'{string} -> {vul.stdout}')
