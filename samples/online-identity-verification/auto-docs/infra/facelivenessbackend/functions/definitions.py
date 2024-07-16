ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/infra/facelivenessbackend/functions/definitions.py

<Template>
## ファイル概要

このファイルは、AWS CDK を使用してAWS Lambdaリソースを定義するための Python クラスを定義しています。
主に aws_cdk ライブラリと constructs ライブラリを使用しています。

## 主要なサブルーチン

### FaceLivenessBackendFunction クラス
- `component_name` プロパティ: ユーザーポータル Lambda 関数のコンポーネント名を返します。
- `function_name` プロパティ: ユーザーポータル Lambda 関数の完全な名前を返します。
- `function_timeout` プロパティ: Lambda 関数のタイムアウト時間を返します。
- `__init__` メソッド: Lambda 関数を初期化し、必要な IAM ポリシーをアタッチします。

### FaceLivenessStartLivenessSession クラス
- `source_directory` プロパティ: ソースコードのディレクトリを返します。
- `component_name` プロパティ: コンポーネント名を返します。

### FaceLivenessSessionResult クラス
- `source_directory` プロパティ: ソースコードのディレクトリを返します。
- `component_name` プロパティ: コンポーネント名を返します。
- `__init__` メソッド: AmazonS3FullAccess の IAM ポリシーをアタッチします。

### UploadSignUrl クラス 
- `source_directory` プロパティ: ソースコードのディレクトリを返します。
- `component_name` プロパティ: コンポーネント名を返します。
- `__init__` メソッド: AmazonS3FullAccess の IAM ポリシーをアタッチします。

### GetComparefaceResult クラス
- `source_directory` プロパティ: ソースコードのディレクトリを返します。
- `component_name` プロパティ: コンポーネント名を返します。
- `__init__` メソッド: AmazonS3FullAccess と AmazonRekognitionFullAccess の IAM ポリシーをアタッチします。

## データ構造

特に定義されたデータ構造はありません。

## 主要なアルゴリズム

特徴的なアルゴリズムやロジックは記述されていません。

## 入出力

Lambda 関数の入出力は記述されていません。

## 利用している外部モジュールやライブラリの説明

- aws_cdk: AWS Cloud Development Kit (CDK) を使用するためのモジュール
- constructs: AWS CDK で使用される基本的なコンストラクトを提供するモジュール
- aws_iam: AWS Identity and Access Management (IAM) リソースを定義するためのモジュール

## エラー処理の方法

エラー処理の方法は記述されていません。

</Template>