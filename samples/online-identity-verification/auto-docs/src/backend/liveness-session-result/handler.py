## ファイル概要

このファイルは、Amazon Rekognition FaceLivenessDetectionのセッション結果を取得し、処理するためのLambda関数です。
主に利用しているサービスはAmazon Rekognition、Amazon S3です。

## 主要なサブルーチン

### get_session_results(event)
- Amazon Rekognition FaceLivenessDetectionのセッション結果を取得する
- 引数: event (セッションIDを含むdict)
- 戻り値: セッション結果(dict)
- グローバル変数: rek_client (Rekognitionクライアント)、s3_client (S3クライアント)

### lambda_handler(event, context)
- Lambda関数のハンドラー
- get_session_resultsの結果を返す
- 引数: event (セッションIDを含むdict)、context (LambdaContextオブジェクトInfo)
- 戻り値: ステータスコード200とセッション結果をbodyに含むdict

## データ構造

- event (dict): セッションIDを含む
- 応答 (dict): Rekognitionからの応答データ

## 主要なアルゴリズム

- get_session_resultsでRekognitionのセッション結果を取得
- 参照画像をS3にアップロードし、Base64エンコーディング

## 入出力  

- 入力: LambdaのイベントからセッションID
- 出力: セッション結果(dict)
- S3バケット: 環境変数FACELIVENESS_BUCKETで指定されたバケットに参照画像をアップロード

## 利用している外部モジュールやライブラリの説明

- boto3: AWS SDKライブラリ(Rekognition、S3の操作に使用)
- io: バイトストリームの操作に使用  
- os: 環境変数の取得に使用
- sys: コマンドライン引数の取得に使用
- base64: 画像データのBase64エンコーディングに使用
- logging: ログ出力に使用

## エラー処理の方法

RekognitionのさまざまなException(アクセス拒否、パラメータエラーなど)をキャッチし、FaceLivenessErrorをスローします。