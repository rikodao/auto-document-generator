ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/infra/default_lambda.py

<Template>
## ファイル概要

このファイルは、AWS CDK (Cloud Development Kit) を使用して、AWS Lambda 関数をデプロイするための Python コードを含んでいます。主な機能は以下の通りです:

- AWS Lambda 関数のデプロイ
- AWS IAM ロールの作成
- 共有の依存関係 (requirements.txt) の管理
- レイヤーを使用した依存関係のインストール

このファイルは、`aws_cdk` および `constructs` ライブラリを使用しています。

## 主要なサブルーチン

### `DefaultFunction` クラス
- `source_directory` プロパティ: ソースコードのディレクトリパスを返す (実装が必要)
- `component_name` プロパティ: コンポーネント名を返す
- `function_name` プロパティ: Lambda 関数名を返す (実装が必要)
- `rfl_stack` プロパティ: `IRflStack` インスタンスを返す
- `function_timeout` プロパティ: Lambda 関数のタイムアウト時間を返す
- `function` プロパティ: `lambda_.IFunction` インスタンスを返す/設定する
- `__init__` メソッド: コンストラクタ、IAM ロールとLambda 関数を作成する

## データ構造

特に明示的なデータ構造はありません。

## 主要なアルゴリズム

特徴的なアルゴリズムはありません。

## 入出力

- 入力: 環境変数、ソースコードディレクトリ、`requirements.txt` ファイル
- 出力: AWS Lambda 関数、IAM ロール、レイヤー

## 利用している外部モジュールやライブラリの説明

- `aws_cdk`: AWS Cloud Development Kit
- `constructs`: AWS CDK の基本クラス
- `aws_ec2`, `aws_iam`, `aws_lambda`: AWS CDK の各サービスのコンストラクト
- `subprocess`: コマンドラインプログラムの実行
- `os`: オペレーティングシステム機能へのポータブルな方法でアクセスする
- `typing`: 型ヒントのサポート

## エラー処理の方法

明示的なエラー処理は記述されていません。AWS CDK の例外処理に従います。

</Template>