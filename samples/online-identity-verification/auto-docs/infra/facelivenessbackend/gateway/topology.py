ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/infra/facelivenessbackend/gateway/topology.py

<Template>
## ファイル概要

このファイルはAWS CDKを使って、API Gatewayを介して顔認証サービスにアクセスするためのリソースを定義しています。
aws_cdk、aws_iam、aws_apigateway、aws_ssmモジュールがインポートされています。

## 主要なサブルーチン

- __init__(self, scope, id, rfl_stack): コンストラクタ。API Gatewayとそれに紐づくIAMロールを初期化します。
- rest_api_url(self): API Gatewayの URL を返します。
- bind_upload_signed_url(self, functions): アップロードする画像の署名付き URL を取得するためのAPIリソースを設定します。
- bind_start_liveness_session(self, functions): 顔認証セッションを開始するためのAPIリソースを設定します。
- bind_liveness_session_result(self, functions): 顔認証セッションの結果を取得するためのAPIリソースを設定します。
- bind_get_compareface_result(self, functions): 顔比較の結果を取得するためのAPIリソースを設定します。
- __bind_lambda_function(self, resource_name, function, integration_http_method, proxy=False): Lambda関数をAPIリソースにバインドするための内部メソッド。

## データ構造

特になし

## 主要なアルゴリズム

特になし

## 入出力

API Gateway経由で以下のリソースにアクセスできます。
- /uploadsignedurl (GET): 画像のアップロード用の署名付きURLを取得
- /createfacelivenesssession (GET): 顔認証セッションを開始
- /getfacelivenesssessionresults (POST): 顔認証セッションの結果を取得
- /getcomparefaceresult (GET): 顔比較の結果を取得

## 利用している外部モジュールやライブラリの説明

- aws_cdk: AWS Cloud Development Kitライブラリ
- aws_iam: AWS Identity and Access Management (IAM) サービスを操作するためのライブラリ
- aws_apigateway: AWS API Gatewayサービスを操作するためのライブラリ
- aws_ssm: AWS Systems Manager (SSM) サービスを操作するためのライブラリ

## エラー処理の方法

API Gateway側で以下のようなレスポンスを返すよう設定されています。
- 200: 正常レスポンス
- 500: エラーレスポンス (application/jsonモデルを使用)

</Template>