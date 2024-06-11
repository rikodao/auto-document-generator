```python
<Template>
## ファイル概要

このファイルはAWS LambdaのPython関数で、顔認識サービスAWS Rekognitionを使って2つの顔画像を比較し、類似度スコアを返す役割を持つ。
関連するAWSサービスはS3、Rekognitionが使われている。

## 主要なサブルーチン

1. S3Manager.generate_presigned_url(key)
  - 引数: key (str) - S3オブジェクトのキー
  - 戻り値: (str) - 署名付きURLまたはNone
  - S3オブジェクトの署名付き一時URLを生成する

2. RekognitionManager.compare_faces(sessionid, similarity_threshold=50)
  - 引数: sessionid (str) - セッションID, similarity_threshold (int) - 類似度スレショルド 
  - 戻り値: (dict) - Rekognitionの比較結果またはNone
  - 2つの顔画像をRekognitionで比較し、類似度スコアを含む結果を返す

3. lambda_handler(event, context)
  - 引数: event (dict) - Lambda呼び出しイベント, context (dict) - Lambda呼び出しコンテキスト
  - 戻り値: (dict) - APIGatewayの応答
  - メイン関数。セッションIDからS3の画像URLを取得し、Rekognitionで比較、結果を返す

## データ構造

特になし

## 主要なアルゴリズム  

特になし

## 入出力

- 入力: AWS Lambda呼び出しイベントからクエリ文字列のセッションIDを取得
- 出力: APIGatewayレスポンス (JSON形式)
  - croppedImage: 顔画像のS3署名付きURL  
  - similarityScore: 類似度スコア (0-100)

## 利用している外部モジュールやライブラリの説明

- boto3: AWS SDKライブラリ。S3、Rekognitionにアクセスするため使用
- os: 環境変数を取得するため使用  
- json: JSON形式のレスポンスを生成するため使用
- logging: ロギングするため使用

## エラー処理の方法

- S3の署名付きURLの生成に失敗した場合、例外を送出
- Rekognitionの顔比較に失敗した場合、例外を送出
- Lambda内でキャッチされた例外はAPIGatewayレスポンスの'error'キーに格納される

## その他

特になし

</Template>
```