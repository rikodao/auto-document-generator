import os
import boto3
import json
from botocore.exceptions import ClientError

def write_response_to_file(file_path, response_text):
    """
    レスポンスの内容をファイルに書き込む関数

    Args:
        file_path (str): 元のファイルのパス
        response_text (str): APIからのレスポンスの内容

    Returns:
        None

    この関数は、以下の処理を行います:
    1. 実行プログラムの直下に 'auto-docs' というディレクトリを作成する
    2. 'auto-docs' ディレクトリ内に、元のファイルと同じディレクトリ構造を維持したファイルを作成する
    3. 作成したファイルに、APIからのレスポンスの内容を書き込む
    """
    docs_dir = os.path.join(os.getcwd(), 'auto-docs')
    os.makedirs(docs_dir, exist_ok=True)

    relative_path = os.path.relpath(file_path, os.getcwd())
    docs_file_path = os.path.join(docs_dir, relative_path)
    os.makedirs(os.path.dirname(docs_file_path), exist_ok=True)

    with open(docs_file_path, 'w') as docs_file:
        # print("docs_file_path")
        # print(docs_file_path)
        # print("response_text")
        # print(response_text)
        # print("---------------------------------------------------------------------------------------")

        docs_file.write("ファイルパス: "+ file_path +  "\n\n" + response_text)


def get_response_from_bedrock(file_content, model_id, system_prompt, max_tokens):
    """
    ファイルの内容をBedrockモデルに送信し、レスポンスを取得する関数

    Args:
        file_content (str): 処理対象のファイルの内容
        model_id (str): 使用するBedrockモデルのID
        system_prompt (str): モデルに与える初期のプロンプト
        max_tokens (int): 生成されるレスポンスの最大トークン数

    Returns:
        str: モデルから生成されたレスポンス

    この関数は、以下の処理を行います:
    1. Bedrockランタイムのクライアントオブジェクトを作成する
    2. ファイルの内容をユーザーメッセージとして設定する
    3. 入力データをJSON形式に変換する
    4. Bedrockモデルに入力を送信し、レスポンスを取得する
    5. レスポンスからテキストを抽出する
    6. 抽出したテキストを返す
    """
    bedrock_runtime = boto3.client('bedrock-runtime')

    user_message = {"role": "user", "content": file_content}
    messages = [user_message]

    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": max_tokens,
        "system": system_prompt,
        "messages": messages
    })

    response = bedrock_runtime.invoke_model(body=body, modelId=model_id)
    response_body = json.loads(response.get('body').read())
    answer = response_body["content"][0]["text"]

    return answer

def write_error_to_file(file_path, error_message):
    """
    エラーメッセージをファイルに書き込む関数

    Args:
        file_path (str): 元のファイルのパス
        error_message (str): エラーメッセージ

    Returns:
        None

    この関数は、以下の処理を行います:
    1. 実行プログラムの直下に 'error-docs' というディレクトリを作成する
    2. 'error-docs' ディレクトリ内に、元のファイルと同じディレクトリ構造を維持したファイルを作成する
    3. 作成したファイルに、エラーメッセージを書き込む
    """
    error_dir = os.path.join(os.getcwd(), 'auto-docs-error')
    os.makedirs(error_dir, exist_ok=True)

    relative_path = os.path.relpath(file_path, os.getcwd())
    error_file_path = os.path.join(error_dir, relative_path)
    os.makedirs(os.path.dirname(error_file_path), exist_ok=True)

    with open(error_file_path, 'w') as error_file:
        error_file.write(error_message)

def process_file(file_path, model_id, system_prompt, max_tokens):
    """
    ファイルを処理する関数

    Args:
        file_path (str): 処理対象のファイルのパス
        model_id (str): 使用するBedrockモデルのID
        system_prompt (str): モデルに与える初期のプロンプト
        max_tokens (int): 生成されるレスポンスの最大トークン数

    Returns:
        None

    この関数は、以下の処理を行います:
    1. 指定されたファイルを読み込む
    2. ファイルの内容をBedrockモデルに送信し、レスポンスを取得する
    3. レスポンスの内容をファイルに書き込む
    4. エラーが発生した場合は、エラーメッセージをファイルに書き込む
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        response = get_response_from_bedrock(content, model_id, system_prompt, max_tokens)
        write_response_to_file(file_path, response)
    except ClientError as e:
        error_message = f"Error: {e.response['Error']['Code']}: {e.response['Error']['Message']}"
        write_error_to_file(file_path, error_message)

def traverse_directory(directory, model_id, system_prompt, max_tokens, file_extention):
    """
    ディレクトリ内のファイルを再帰的に処理する関数

    Args:
        directory (str): 処理対象のディレクトリのパス
        model_id (str): 使用するBedrockモデルのID
        system_prompt (str): モデルに与える初期のプロンプト
        max_tokens (int): 生成されるレスポンスの最大トークン数

    Returns:
        None

    この関数は、以下の処理を行います:
    1. 指定されたディレクトリ内のすべてのファイルを再帰的に探索する
    2. 見つかったファイルごとに、process_file関数を呼び出して処理を行う
    """
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != 'auto-docs']  # 'auto-docs' ディレクトリを無視する
        for file in files:
            file_path = os.path.join(root, file)
            if '/.' not in file_path and file_path.endswith(file_extention):  # 不可視ファイルとディレクトリを除く。file_extention定義の対象拡張子ファイルのみ
                print(file_path)
                process_file(file_path, model_id, system_prompt, max_tokens)

# 使用例
current_dir = os.getcwd()
model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
file_extention=('.py', '.java', '.cpp', '.cc', '.cxx', '.c', '.cs', '.php', '.rb', '.js', '.ts', '.kt', '.swift', '.go', '.rs', '.pl', '.sh', '.vb', '.m', '.r', '.scala', '.hs', '.clj', '.ex', '.exs', '.fs', '.jl', '.lua', '.nim', '.html', '.htm', '.css', '.jsp', '.asp', '.aspx', '.csv', '.json', '.xml', '.sql')
system_prompt = """
あなたは優秀なシステムエンジニアです。
現在javascriptとpythonで書かれたシステムがあるのですが、知見がある人間が 全員退職してしまって、ソースコードを解き明かす必要があります。
そのためにプログラム概要書を作る必要があるのですが、以下のテンプレートに沿って、ユーザープロンプトに入ってくるソースコードを基に十分な情報量を持ったプログラム概要書を出力してください。プログラム概要書以外の余計な出力はしないでください。

<Template>
## ファイル概要

ファイルの役割と機能の簡単な説明
関連するモジュールやパッケージ

## 主要なサブルーチン

サブルーチン名と機能の簡単な説明
引数と戻り値の説明
グローバル変数の使用状況

## データ構造

ファイル内で使用されるデータ構造の説明
レコード構造やハッシュ、配列などの詳細

## 主要なアルゴリズム

特徴的なアルゴリズムやロジックの説明
特殊な計算式やパターンマッチングの説明

## 入出力

入力ファイル、出力ファイル、データベースアクセスの説明
入出力フォーマットやプロトコルの説明
外部モジュールの利用

## 利用している外部モジュールやライブラリの説明
呼び出し方法と利用目的の説明
注意事項

## エラー処理の方法
並列実行時の留意点
その他の制約条件や前提条件
</Template>
"""
max_tokens = 200000

traverse_directory(current_dir, model_id, system_prompt, max_tokens, file_extention)