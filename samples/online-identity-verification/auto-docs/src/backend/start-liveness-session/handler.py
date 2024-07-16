ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/src/backend/start-liveness-session/handler.py

```python
<Template>
## ファイル概要

このファイルは、Amazon Rekognition サービスを使用して顔の生存性検出セッションを作成するためのものです。
boto3 パッケージと logging モジュールを使用しています。

## 主要なサブルーチン

### create_session()
- 機能: Amazon Rekognition の create_face_liveness_session() API を呼び出して、生存性検出セッションを作成します。
- 引数: なし
- 戻り値: セッション ID (文字列)
- グローバル変数の使用: rek_client、logger

### lambda_handler(event, context)
- 機能: AWS Lambda 関数のエントリポイントです。create_session() 関数を呼び出し、その結果をレスポンスとして返します。
- 引数: event (dict)、context (object)
- 戻り値: レスポンス (dict)
- グローバル変数の使用: なし

## データ構造

特になし

## 主要なアルゴリズム

特になし

## 入出力

入力:
- なし

出力:
- レスポンス (dict): statusCode (int)、sessionId (str)

外部サービスアクセス:
- Amazon Rekognition サービス

## 利用している外部モジュールやライブラリの説明

- boto3: AWS SDK for Python
- os: オペレーティングシステムに依存する機能を利用するためのモジュール
- logging: ログ出力を行うためのモジュール

## エラー処理の方法

Amazon Rekognition の API から発生する可能性のある例外をキャッチし、カスタム例外 FaceLivenessError を送出しています。

- AccessDeniedException
- InternalServerError
- InvalidParameterException
- ThrottlingException
- ProvisionedThroughputExceededException

その他の制約条件や前提条件:
- FACELIVENESS_BUCKET 環境変数が設定されている必要があります。

</Template>
```