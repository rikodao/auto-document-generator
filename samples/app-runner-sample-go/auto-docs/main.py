ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/app-runner-sample-go/main.py

```
<Template>
## ファイル概要

このファイルは、指定されたディレクトリ内のすべてのファイル（拡張子がfile_extentionで指定された拡張子のものに限る）を処理するためのPythonスクリプトです。
処理には、Amazon Bedrock APIが利用されます。

関連するモジュール:
- os: ディレクトリ操作に使用
- boto3: Bedrock APIとのインターフェースに使用
- json: JSON形式のデータを扱うために使用
- botocore.exceptions: Bedrock APIからのエラー処理に使用

## 主要なサブルーチン

### write_response_to_file(file_path, response_text)
- 機能: レスポンスの内容をファイルに書き込む
- 引数:
  - file_path (str): 元のファイルのパス
  - response_text (str): APIからのレスポンスの内容
- 戻り値: なし
- グローバル変数の使用: なし

### get_response_from_bedrock(file_content, model_id, system_prompt, max_tokens)
- 機能: ファイルの内容をBedrockモデルに送信し、レスポンスを取得する
- 引数:
  - file_content (str): 処理対象のファイルの内容
  - model_id (str): 使用するBedrockモデルのID
  - system_prompt (str): モデルに与える初期のプロンプト
  - max_tokens (int): 生成されるレスポンスの最大トークン数
- 戻り値: str (モデルから生成されたレスポンス)
- グローバル変数の使用: なし

### write_error_to_file(file_path, error_message)
- 機能: エラーメッセージをファイルに書き込む
- 引数:
  - file_path (str): 元のファイルのパス
  - error_message (str): エラーメッセージ
- 戻り値: なし
- グローバル変数の使用: なし

### process_file(file_path, model_id, system_prompt, max_tokens)
- 機能: ファイルを処理する
- 引数:
  - file_path (str): 処理対象のファイルのパス
  - model_id (str): 使用するBedrockモデルのID
  - system_prompt (str): モデルに与える初期のプロンプト
  - max_tokens (int): 生成されるレスポンスの最大トークン数
- 戻り値: なし
- グローバル変数の使用: なし

### traverse_directory(directory, model_id, system_prompt, max_tokens, file_extention)
- 機能: ディレクトリ内のファイルを再帰的に処理する
- 引数:
  - directory (str): 処理対象のディレクトリのパス
  - model_id (str): 使用するBedrockモデルのID
  - system_prompt (str): モデルに与える初期のプロンプト
  - max_tokens (int): 生成されるレスポンスの最大トークン数
  - file_extention (tuple): 処理対象のファイルの拡張子
- 戻り値: なし
- グローバル変数の使用: なし

## データ構造

特に複雑なデータ構造は使用されていません。
主に文字列やリストなどの標準データ型が使用されています。

## 主要なアルゴリズム

特筆すべきアルゴリズムはありません。
ただし、ディレクトリを再帰的に探索する際に、os.walk関数が使用されています。

## 入出力

入力ファイル: 指定されたディレクトリ内のファイル
出力ファイル: 'auto-docs' ディレクトリ内に、入力ファイルと同じディレクトリ構造で生成されたファイル
データベースアクセス: なし
外部モジュールの利用: Amazon Bedrock API

## 利用している外部モジュールやライブラリの説明

- boto3: Amazon Web Servicesとの連携に使用される、Pythonの公式ライブラリです。本スクリプトでは、Bedrock APIとの通信に使用されています。
- botocore.exceptions: boto3ライブラリが提供するエラー処理用のモジュールです。本スクリプトでは、Bedrock APIからのエラー処理に使用されています。

## エラー処理の方法

エラーが発生した場合は、write_error_to_file関数が呼び出され、エラーメッセージが 'error-docs' ディレクトリ内のファイルに書き込まれます。

並列実行時の留意点: なし
その他の制約条件や前提条件: なし
</Template>
```