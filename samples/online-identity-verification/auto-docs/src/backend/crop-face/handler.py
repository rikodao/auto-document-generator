ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/src/backend/crop-face/handler.py

```python
<Template>
## ファイル概要

このファイルは、AWSのS3バケットにアップロードされた画像から顔を検出し、その顔の部分を切り抜いた画像をS3の別のバケットにアップロードするLambda関数です。
boto3およびPILライブラリを使用しています。

## 主要なサブルーチン

### lambda_handler(event, context)
- 引数: event(S3イベントオブジェクト), context(Lambda実行コンテキスト)
- 戻り値: ステータスコードと実行結果の辞書
- 機能: メイン処理を行う関数です。
  1. S3のイベントから画像のバケット名とキーを取得
  2. S3から画像をダウンロード
  3. Rekognitionで画像から顔を検出
  4. 検出された顔の部分を切り抜き
  5. 切り抜いた顔の画像を別のS3バケットにアップロード

## データ構造

特に複雑なデータ構造は使用されていません。
主に辞書やリスト、バイト配列を使用しています。

## 主要なアルゴリズム

特徴的なアルゴリズムはありません。
Rekognitionの顔検出APIとPILライブラリの画像処理機能を利用しています。

## 入出力

- 入力: S3バケットにアップロードされた画像ファイル
- 出力: 切り抜いた顔の画像ファイル (別のS3バケットにアップロード)

## 利用している外部モジュールやライブラリの説明

- boto3: AWS SDKのPythonライブラリ。S3およびRekognitionサービスを利用するために使用されています。
- PIL (Python Imaging Library): 画像処理ライブラリ。画像の切り抜きに使用されています。

## エラー処理の方法

顔が検出されなかった場合は、ステータスコード400とエラーメッセージを返します。
その他の例外処理は特に記述されていません。
</Template>
```