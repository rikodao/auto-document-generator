ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/main.py

<Template>
## ファイル概要

このファイルは、ディレクトリ内のファイルを再帰的に処理し、それらのファイルの内容をBedrockモデルに送信し、応答を取得する役割を持っています。また、応答の内容をファイルに書き込む機能も備えています。
関連するモジュールやパッケージは、os、boto3、json、botocore.exceptionsからインポートされています。

## 主要なサブルーチン

1. write_response_to_file(file_path, response_text):
   - 機能: レスポンスの内容をファイルに書き込む
   - 引数: file_path (str) - 元のファイルのパス、response_text (str) - APIからのレスポンスの内容
   - 戻り値: なし
   - グローバル変数の使用: なし

2. get_response_from_bedrock(file_content, model_id, system_prompt, max_tokens):
   - 機能: ファイルの内容をBedrockモデルに送信し、レスポンスを取得する
   - 引数: file_content (str) - 処理対象のファイルの内容、model_id (str) - 使用するBedrockモデルのID、system_prompt (str) - モデルに与える初期のプロンプト、max_tokens (int) - 生成されるレスポンスの最大トークン数
   - 戻り値: str - モデルから生成されたレスポンス
   - グローバル変数の使用: なし

3. write_error_to_file(file_path, error_message):
   - 機能: エラーメッセージをファイルに書き込む
   - 引数: file_path (str) - 元のファイルのパス、error_message (str) - エラーメッセージ
   - 戻り値: なし
   - グローバル変数の使用: なし

4. process_file(file_path, model_id, system_prompt, max_tokens):
   - 機能: ファイルを処理する
   - 引数: file_path (str) - 処理対象のファイルのパス、model_id (str) - 使用するBedrockモデルのID、system_prompt (str) - モデルに与える初期のプロンプト、max_tokens (int) - 生成されるレスポンスの最大トークン数
   - 戻り値: なし
   - グローバル変数の使用: なし

5. traverse_directory(directory, model_id, system_prompt, max_tokens, file_extention):
   - 機能: ディレクトリ内のファイルを再帰的に処理する
   - 引数: directory (str) - 処理対象のディレクトリのパス、model_id (str) - 使用するBedrockモデルのID、system_prompt (str) - モデルに与える初期のプロンプト、max_tokens (int) - 生成されるレスポンスの最大トークン数
   - 戻り値: なし
   - グローバル変数の使用: なし

## データ構造

ファイル内で使用されるデータ構造は、文字列、リスト、ディクショナリがあります。

## 主要なアルゴリズム

特に特徴的なアルゴリズムはありませんが、ディレクトリ内のファイルを再帰的に探索するためのos.walkを利用しています。また、Bedrockランタイムのクライアントを作成し、入力データをJSONに変換して送信し、レスポンスを取得するロジックがあります。

## 入出力

入力は、処理対象のファイルの内容とBedrockモデルのIDやプロンプトなどの設定値です。
出力は、レスポンスの内容やエラーメッセージがファイルに書き込まれます。
外部モジュールの利用として、boto3を使ってBedrockランタイムにアクセスしています。

## 利用している外部モジュールやライブラリの説明

1. os: オペレーティングシステムの機能にアクセスするためのモジュール。ディレクトリの作成やファイルパスの操作に使用されています。

2. boto3: AWS SDKのPythonライブラリ。Bedrockランタイムにアクセスするためのクライアントを作成するのに使用されています。

3. json: JSON形式のデータを扱うためのモジュール。入力データをJSON形式に変換するのに使用されています。

4. botocore.exceptions: boto3で発生する例外を扱うためのモジュール。Bedrockランタイムへのリクエストでエラーが発生した場合に使用されています。

## エラー処理の方法

ClientErrorの例外をキャッチし、エラーメッセージをファイルに書き込むようになっています。
並列実行時の留意点や制約条件については特に記載されていません。

</Template>