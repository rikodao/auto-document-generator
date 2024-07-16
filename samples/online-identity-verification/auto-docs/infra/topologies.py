ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/infra/topologies.py

<Template>
## ファイル概要

このファイルは、AWS Cloud Development Kit (CDK) を使用して、Face Liveness アプリケーションのインフラストラクチャをデプロイするための CDK スタックを定義しています。主な機能は以下の通りです。

- Amazon Cognito ユーザープールの設定
- Face Liveness バックエンドサービスのデプロイ
- Face Liveness フロントエンド Web アプリケーションのデプロイ
- AWS Amplify を使用したフロントエンドビルドとデプロイの管理

## 主要なサブルーチン

- `__init__(self, scope: Construct, id: str, rfl_stack_name: str, **kwargs)` - コンストラクタ。引数には CDK スコープ、ID、スタック名が渡されます。

## データ構造

特に複雑なデータ構造は使用されていません。

## 主要なアルゴリズム

特筆すべきアルゴリズムはありません。

## 入出力

入力ファイルや出力ファイルはありません。

## 利用している外部モジュールやライブラリの説明

- `aws_cdk` - AWS Cloud Development Kit
- `infra.facelivenessbackend.topology` - Face Liveness バックエンドサービスのデプロイ用モジュール
- `infra.interfaces` - インターフェース定義モジュール
- `infra.cropface.topology` - Crop Face サービスのデプロイ用モジュール
- `infra.frontend.topology` - Face Liveness フロントエンド Web アプリケーションのデプロイ用モジュール
- `infra.frontend.cognito.topology` - Amazon Cognito ユーザープールの設定用モジュール

## エラー処理の方法

特別なエラー処理は実装されていません。

</Template>