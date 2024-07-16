ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/infra/facelivenessbackend/topology.py

```python
<Template>
## ファイル概要

このファイルは、顔認証に関連するさまざまなサービスを構築するためのAWS Cloud Development Kit (CDK)アプリケーションのコードです。主な機能は以下の通りです:

- FaceLivenessBucketSetの作成
- FaceLivenessFunctionSetの宣言
- FaceLivenessGatewayの作成
- 各サービス間の結合

関連するモジュールやパッケージは、aws-cdkおよびその他のAWSサービスのパッケージです。

## 主要なサブルーチン

1. `__init__(self, scope: Construct, id: builtins.str, rfl_stack:IRflStack, cropface: CropFace)`:
   - コンストラクタ
   - 引数は親スコープ、ID、RFLスタック、CropFaceインスタンス
   - FaceLivenessBucketSet、FaceLivenessFunctionSet、FaceLivenessGatewayを作成し、それらを相互に結合する

## データ構造

特定のデータ構造は使用されていません。

## 主要なアルゴリズム

特筆すべきアルゴリズムはありません。

## 入出力

入出力ファイルや外部データベースへのアクセスはありません。

## 利用している外部モジュールやライブラリの説明

- aws-cdk: AWSサービスをコード化するための開発フレームワーク
- 独自のモジュール:
  - `infra.facelivenessbackend.functions.topology`
  - `infra.facelivenessbackend.bucket.topology` 
  - `infra.facelivenessbackend.gateway.topology`
  - `infra.interfaces`
  - `infra.cropface.topology`

## エラー処理の方法

特別なエラー処理は実装されていません。
</Template>
```