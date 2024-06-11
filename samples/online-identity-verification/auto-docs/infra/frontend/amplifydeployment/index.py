## ファイル概要

このスクリプトは、AWS Amplify サービスを操作するための Python プログラムです。主な機能は以下の通りです。

- Amplify アプリケーションの一覧取得
- 指定したアプリケーションの指定ブランチにおけるデプロイジョブの状況監視

AWS Boto3 ライブラリを使用して Amplify クライアントを作成し、API 呼び出しを行っています。

## 主要なサブルーチン

### lambda_handler(event, context)
- 引数: event (dict), context (object)
- 戻り値: dict
- 機能: Lambda 関数のエントリポイント。指定されたアプリケーションとブランチのデプロイジョブを監視する。

### getApp(name)
- 引数: name (str)
- 戻り値: tuple (appName, appId)
- 機能: 指定された名前のアプリケーションを取得する。アプリケーション名とIDを返す。

### getBranch(appId, name)
- 引数: appId (str), name (str)
- 戻り値: str
- 機能: 指定されたアプリケーションIDとブランチ名からブランチ情報を取得する。

### getJob(appId, branch)
- 引数: appId (str), branch (str)
- 戻り値: str or None
- 機能: 指定されたアプリケーションIDとブランチ名から、進行中のデプロイジョブIDを取得する。

## データ構造

特に複雑なデータ構造は使用されていません。AWS API から返される JSON データを Python の dict と list で扱っています。

## 主要なアルゴリズム

特徴的なアルゴリズムはありません。AWS API を呼び出して情報を取得し、ループ処理でデプロイジョブの状態を監視するロジックになっています。

## 入出力

### 入力
- event (dict): Lambda 関数の入力イベントデータ。アプリケーション名とブランチ名を含む。

### 出力
- dict: デプロイ状況を示すメッセージを含む辞書が返される。

外部データの入出力はありません。

## 利用している外部モジュールやライブラリの説明

- boto3: AWS SDK for Python。Amplify クライアントを作成し、API を呼び出すために使用される。
- botocore.exceptions: boto3 のエラー処理のためのモジュール。

## エラー処理の方法

特別なエラー処理は実装されていません。AWS API からの例外は発生次第終了します。