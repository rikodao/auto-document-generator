ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/infra/cropface/topology.py

<Template>
## ファイル概要

このファイルは、AWS CDKを使ってAWS上にリソースを構築するためのコードです。
主な機能は以下の通りです:

- S3バケットの作成(識別カード画像用、加工済み顔画像用)
- Lambda関数の作成(顔画像加工用)
- S3バケットとLambda関数の連携

aws_cdk、constructs、aws_s3、aws_s3_notifications、aws_iam、aws_lambda、aws_ecr_assetsなどのモジュールをインポートしています。

## 主要なサブルーチン

CropFace
- コンストラクタで以下のリソースを作成します:
    - S3バケット(識別カード画像用)
    - S3バケット(加工済み顔画像用)
    - IAMロール(LambdaがECRにアクセスするため)
    - DockerイメージからLambda関数を作成
    - LambdaにIAMポリシーをアタッチ
    - S3バケットとLambda関数を連携

## データ構造

特に複雑なデータ構造は使用されていません。

## 主要なアルゴリズム

特徴的なアルゴリズムはありません。

## 入出力

- 入力: S3バケットに識別カード画像がアップロードされる
- 出力: 顔部分を切り抜いた画像がS3バケットに出力される

## 利用している外部モジュールやライブラリの説明

- aws_cdk: AWS Cloud Development Kitを使ってAWS上のリソースを定義
- aws_s3: S3バケットを作成するため
- aws_lambda: Lambda関数を作成するため
- aws_ecr_assets: ECRからDockerイメージを取得するため
- aws_iam: IAMロールを作成するため

## エラー処理の方法

特にエラー処理のロジックは記載されていません。
CDKのデプロイ時にエラーが発生した場合はCloudFormationのイベントでエラー内容を確認する必要があります。

</Template>