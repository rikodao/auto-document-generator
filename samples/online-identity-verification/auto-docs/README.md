## ファイル概要

このコードは、Amazon Rekognitionを使ったオンラインIDの本人確認フローを実装するサンプルコードです。DetectFace、CompareFace、Face Livenessを使って、本物のユーザーを検出し、デッドプロセスによる不正な偽装を数秒で検出し、本人確認書類の顔画像とユーザーの顔が一致するかチェックします。

## 主要なサブルーチン

- `start-liveness-session`
    - Face Livenessセッションを開始するバックエンド
    - 引数: ユーザーID、本人確認書類の顔画像のS3パス
    - 戻り値: セッションIDとセッションデータ
    - AWS SDK、RekognitionClientを使用
- `liveness-session-result`
    - Face Livenessセッションの結果を取得するバックエンド
    - 引数: セッションID
    - 戻り値: セッション結果(承認/不承認)
    - AWS SDK、RekognitionClientを使用

## データ構造

- セッションデータ
    - ユーザーID、本人確認書類の顔画像のS3パス、セッションIDなどを含む

## 主要なアルゴリズム

- Amazon Rekognition DetectFace
    - 本人確認書類から顔画像を切り出す
- Amazon Rekognition CompareFace 
    - ユーザーの顔と本人確認書類の顔が一致するかチェック
- Amazon Rekognition Face Liveness
    - リアルタイムにユーザーの顔の動きを追跡し、偽装でないかチェック

## 入出力

- 入力: ユーザーID、本人確認書類の画像ファイル
- 出力: セッション結果(承認/不承認)
- AWS S3にデータを読み書き
- AWS APIゲートウェイを使ってフロントエンドと通信

## 利用している外部モジュールやライブラリの説明

- AWS Amplify SDK
    - フロントエンドでAWS APIを呼び出すため
- AWS SDK for Python
    - バックエンドでAWS APIを呼び出すため 
- React
    - フロントエンドUIフレームワーク

## エラー処理の方法

- バックエンドではAWS LambdaとAWS Cloud Watch Logsでエラー監視
- フロントエンドではエラーハンドリングロジックを実装
- 分散トレース(AWS X-Ray)を使ってリクエストを追跡可能