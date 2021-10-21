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
cmd1 = ["echo", str(string)]
cmd2 = "rev"
# subprocessでコマンドの実行
proc1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
proc2 = subprocess.Popen(cmd2, stdin=proc1.stdout)

# レスポンスヘッダの返却
print('Content-type: text/html; charset=UTF-8')
print('')
# レスポンスボディの返却
print(f'{string} -> {proc2}')
