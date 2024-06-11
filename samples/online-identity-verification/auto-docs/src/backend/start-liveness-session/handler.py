<Template>
## ファイル概要

このファイルは、Amazon Rekognition サービスの Face Liveness 機能を利用するための Lambda 関数です。
主な機能は、新しい Face Liveness セッションを作成することです。
boto3 (AWS SDK for Python) とロギングモジュールを使用しています。

## 主要なサブルーチン

### create_session()
- Face Liveness セッションを作成し、セッション ID を返します。
- 引数: なし
- 戻り値: セッション ID (文字列)
- グローバル変数: rek_client (Rekognition クライアント)、logger (ロガー)
- 例外処理: AccessDeniedException、InternalServerError、InvalidParameterException、ThrottlingException、ProvisionedThroughputExceededException

### lambda_handler(event, context)
- Lambda 関数のメインハンドラー
- 引数: event (Lambda 呼び出しイベントデータ)、context (Lambda コンテキストオブジェクト)
- 戻り値: セッション ID を含む JSON レスポンス

## データ構造

- FaceLivenessError: 独自の例外クラス

## 主要なアルゴリズム

特になし

## 入出力

- 入力: なし
- 出力: セッション ID を含む JSON レスポンス

## 利用している外部モジュールやライブラリの説明

- boto3: AWS SDK for Python
- os: オペレーティングシステム関連の操作
- logging: ロギング機能

## エラー処理の方法

create_session() 関数内で、以下の例外を捕捉し、FaceLivenessError 例外をスローします。
- AccessDeniedException
- InternalServerError
- InvalidParameterException
- ThrottlingException
- ProvisionedThroughputExceededException

## その他

- 環境変数 'FACELIVENESS_BUCKET' を参照しますが、この例では使用されていません。
</Template>