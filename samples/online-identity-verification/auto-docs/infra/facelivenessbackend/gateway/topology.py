## ファイル概要

このファイルは、AWS CDKを使って顔認証APIのためのAPI Gatewayリソースを定義しています。
主な関連モジュールは `aws_cdk`、`aws_iam`、`aws_apigateway`、`aws_ssm`、`constructs` です。

## 主要なサブルーチン

### `__init__`
- コンストラクタ
- API Gatewayとそのための実行ロールを作成します

### `rest_api_url`
- API Gatewayの URL を返します

### `bind_upload_signed_url`
- アップロード用の署名付き URL を取得する API を設定します

### `bind_start_liveness_session` 
- 顔認証セッションを開始する API を設定します  

### `bind_liveness_session_result`
- 顔認証セッション結果を取得する API を設定します

### `bind_get_compareface_result`
- 顔比較結果を取得する API を設定します

### `__bind_lambda_function`
- 共通の Lambda 統合ロジックをカプセル化したプライベート関数です

## データ構造

特に複雑なデータ構造は使われていません。

## 主要なアルゴリズム

特徴的なアルゴリズムはありません。

## 入出力

REST API を介して入出力が行われます。入力はリクエストボディやクエリ文字列パラメータ、出力は JSON 形式のレスポンスです。

## 利用している外部モジュールやライブラリの説明

- `aws_cdk`: AWS Cloud Development Kitのコアモジュール
- `aws_iam`: IAMロールやポリシーを定義するモジュール  
- `aws_apigateway`: API Gatewayリソースを定義するモジュール
- `aws_ssm`: Systems ManagerパラメータストアAPIを操作するモジュール
- `constructs`: CDKアプリの基底クラス

## エラー処理の方法

API Gateway の統合レスポンスで 500 エラーを処理しています。その他の例外処理は明示的に定義されていません。