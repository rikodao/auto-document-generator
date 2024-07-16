ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/app-runner-sample-php/main.py

## ファイル概要

このPythonスクリプトは、指定されたディレクトリ内のファイルを処理し、AnthropicのBedrockモデルを使用してプログラム概要書を生成するための機能を提供しています。
主な使用されているモジュールは、os、boto3、json、botocore.exceptionsです。

## 主要なサブルーチン

### write_response_to_file(file_path, response_text)
- 機能: APIからのレスポンスの内容を指定されたファイルパスに書き込みます。
- 引数:
  - file_path (str): 元のファイルのパス
  - response_text (str): APIからのレスポンスの内容
- 戻り値: なし
- グローバル変数の使用: なし

### get_response_from_bedrock(file_content, model_id, system_prompt, max_tokens)
- 機能: ファイルの内容をBedrockモデルに送信し、レスポンスを取得します。
- 引数:
  - file_content (str): 処理対象のファイルの内容
  - model_id (str): 使用するBedrockモデルのID
  - system_prompt (str): モデルに与える初期のプロンプト
  - max_tokens (int): 生成されるレスポンスの最大トークン数
- 戻り値: str (モデルから生成されたレスポンス)
- グローバル変数の使用: なし

### write_error_to_file(file_path, error_message)
- 機能: エラーメッセージを指定されたファイルパスに書き込みます。
- 引数:
  - file_path (str): 元のファイルのパス
  - error_message (str): エラーメッセージ
- 戻り値: なし
- グローバル変数の使用: なし

### process_file(file_path, model_id, system_prompt, max_tokens)
- 機能: ファイルを処理し、Bedrockモデルを使用してプログラム概要書を生成します。
- 引数:
  - file_path (str): 処理対象のファイルのパス
  - model_id (str): 使用するBedrockモデルのID
  - system_prompt (str): モデルに与える初期のプロンプト
  - max_tokens (int): 生成されるレスポンスの最大トークン数
- 戻り値: なし
- グローバル変数の使用: なし

### traverse_directory(directory, model_id, system_prompt, max_tokens, file_extention)
- 機能: ディレクトリ内のファイルを再帰的に処理します。
- 引数:
  - directory (str): 処理対象のディレクトリのパス
  - model_id (str): 使用するBedrockモデルのID
  - system_prompt (str): モデルに与える初期のプロンプト
  - max_tokens (int): 生成されるレスポンスの最大トークン数
  - file_extention (tuple): 処理対象のファイル拡張子
- 戻り値: なし
- グローバル変数の使用: なし

## データ構造

特に複雑なデータ構造は使用されていません。主に文字列、リスト、ディクショナリが使用されています。

## 主要なアルゴリズム

特筆すべきアルゴリズムは使用されていません。ディレクトリ内のファイルの再帰的な探索と処理が行われています。

## 入出力

- 入力: 指定されたディレクトリ内のファイル
- 出力:
  - 'auto-docs' ディレクトリ内に、元のファイルと同じディレクトリ構造を維持したファイルが作成され、その中にBedrockモデルからのレスポンスが書き込まれます。
  - 'auto-docs-error' ディレクトリ内に、エラーが発生した場合のエラーメッセージが書き込まれます。

## 利用している外部モジュールやライブラリの説明

- os: オペレーティングシステムの機能にアクセスするためのモジュール
- boto3: AWS SDKのPythonインターフェース
- json: JSON形式のデータを処理するためのモジュール
- botocore.exceptions: AWS SDKのエラー処理に関するモジュール

## エラー処理の方法

ClientErrorがキャッチされ、エラーメッセージが 'auto-docs-error' ディレクトリ内のファイルに書き込まれます。

## 並列実行時の留意点

特に並列実行に関する処理は含まれていません。

## その他の制約条件や前提条件

- Bedrockモデルへのアクセスが必要です。
- 処理対象のファイルが指定された拡張子のいずれかを持つことが前提となっています。