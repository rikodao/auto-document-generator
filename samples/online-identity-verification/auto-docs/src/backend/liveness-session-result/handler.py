ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/src/backend/liveness-session-result/handler.py

```python
<Template>
## ファイル概要

このファイルはAWS Lambda関数として実行され、Amazon RekognitionのFace Liveness検出機能を利用しています。
Face Livenessとは、顔画像が本物の人物のものであるかを判定する機能です。
boto3ライブラリを使用してAWS RekognitionおよびS3にアクセスしています。

## 主要なサブルーチン

### get_session_results(event)
- 引数: event (dict) - セッションIDを含むイベントデータ
- 戻り値: Rekognition Face Liveness検出の結果
- 機能: Face Livenessセッションの結果を取得し、リファレンス画像をS3にアップロードします。
- グローバル変数: rek_client, s3_client, logger

### lambda_handler(event, context)
- 引数: event (dict), context (dict) - Lambda関数の標準引数
- 戻り値: Face Liveness検出結果を含む応答オブジェクト
- 機能: get_session_resultsを呼び出し、その結果を返します。

## データ構造

このファイルでは独自のデータ構造は定義されていません。
Rekognitionの応答データはdictで表現されています。

## 主要なアルゴリズム

特別な独自のアルゴリズムは実装されていません。
Face Livenessの検出はAWS Rekognitionサービスに委ねられています。

## 入出力

入力:
- Lambdaのイベントオブジェクト(dict) - Face Livenessセッション IDを含む

出力:
- Lambdaの応答オブジェクト(dict) - Face Liveness検出結果を含む

データベース:
- S3バケット - リファレンス画像をアップロードするために使用

## 利用している外部モジュールやライブラリの説明

boto3 - AWS SDKのPythonラッパー
io - バイトストリームの操作
os - オペレーティングシステム機能にアクセス
sys - インタープリタの機能にアクセス 
base64 - Base64エンコーディング/デコーディング
logging - ログ出力

## エラー処理の方法

RekognitionのさまざまなエラーをFaceLivenessErrorとしてラップし、例外処理しています。
ログ出力にloggerを使用しています。

</Template>
```