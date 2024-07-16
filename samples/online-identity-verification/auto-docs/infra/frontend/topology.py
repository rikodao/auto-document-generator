ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/infra/frontend/topology.py

<Template>
## ファイル概要

このコードは、AWS CDKを使用してAWS Amplifyアプリケーションとそれに関連するリソースをデプロイするための機能を提供しています。
主要なモジュールとして、aws_cdk、aws_lambda、aws_codecommit、aws_amplify_alphaなどが使用されています。

## 主要なサブルーチン

- FaceLivenessFrontEnd
  - AWSAmplifyアプリケーションを作成し、環境変数を設定します。
  - 引数: scope, id, rfl_stack, apigateway, cognito
  - グローバル変数: なし

- TriggerFrontEndBuild  
  - Amplifyアプリケーションのビルドを開始するカスタムリソースを作成します。
  - 引数: scope, id, rfl_stack, amplifyApp
  - グローバル変数: なし

- FaceLivenessFrontEndBuildStatus
  - Amplifyアプリケーションのビルド状況を監視するLambda関数とカスタムリソースを作成します。
  - 引数: scope, id, rfl_stack, amplifyApp, buildTrigger  
  - グローバル変数: なし

## データ構造

特に明示的なデータ構造は使用されていません。

## 主要なアルゴリズム

特徴的なアルゴリズムやロジックはありません。

## 入出力

- 入力: なし
- 出力: Amplifyアプリケーションの環境変数としてAPIゲートウェイのURLが出力されます。

## 利用している外部モジュールやライブラリの説明

- aws_cdk: AWS CDKを使用するためのモジュール
- aws_lambda: AWS Lambdaリソースを作成するためのモジュール
- aws_codecommit: AWS CodeCommitリポジトリを作成するためのモジュール
- aws_amplify_alpha: AWS Amplifyアプリケーションを作成するためのモジュール

## エラー処理の方法

特にエラー処理の記述はありません。

</Template>