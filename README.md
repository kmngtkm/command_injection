# コマンドインジェクション環境

## 前提

* Ubuntu 20.04.3 LTS で検証済み

* python3が使用可能なLinux環境であれば実行可能のはず

## 使い方

1. command_injectionディレクトリに移動

  ```
  $ cd [working directory]/command_injection
  ```

2. command_injectionディレクトリ内でpythonのhttpサーバを立ち上げる

  ```
  $ python3 -m http.server --cgi
  ```

3. ブラウザで```http://127.0.0.1:8000```にアクセスする

4. 【正常動作】入力フォームに任意文字列を入力、"送信"をクリックすると文字列が逆さまに出力される

5. 【実行注意】入力フォームに下記のように攻撃コマンド(例えばyesコマンド)を入力する、rmとか取り返しのつかないコマンドはやめましょう...。

  ```
  適当な文字列; 攻撃コマンド
  ```
