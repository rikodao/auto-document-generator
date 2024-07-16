ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/src/frontend/src/Components/CompareFace.js

<Template>
## ファイル概要

このファイルは、React Componentを定義しており、IDドキュメントの画像と顔の写真を比較し、類似性の評価値を表示する機能を持つ。
AWS Amplifyのコンポーネントライブラリを使用している。

## 主要なサブルーチン

- `checkSimilarity()`
  - サーバーAPIにリクエストを送信し、画像の類似度を取得する
  - `similarityScore`と`croppedImageUrl`の状態を更新する
  - 引数なし
  - 戻り値なし
  - グローバル変数の使用なし

- `resultComponet(similarityScore)`
  - 類似度が計算された後に表示するコンポーネントを返す
  - `similarityScore`: 類似度の値を受け取る
  - コンポーネントを返す

- `checkComponet()`
  - 類似度を計算する前に表示するコンポーネントを返す
  - 引数なし
  - コンポーネントを返す

## データ構造

- `similarityScore` (状態変数): 類似度の値を保持する
- `croppedImageUrl` (状態変数): 切り抜かれた顔画像のURLを保持する
- `checking` (状態変数): 類似度計算中かどうかを保持する

## 主要なアルゴリズム

特になし

## 入出力

- 入力
  - `idImage`: IDドキュメントの画像のURL
  - `faceLivenessAnalysis`: 顔の写真のBase64エンコーディングされたデータ
  - `sessionid`: 類似度計算のセッションID

- 出力
  - 画面にコンポーネントを表示する

- 外部API
  - `${endpoint}getcomparefaceresult`にGETリクエストを送信し、類似度を取得する

## 利用している外部モジュールやライブラリの説明

- `react`: Reactライブラリのフレームワーク
- `@aws-amplify/ui-react`: AWS Amplifyの UIコンポーネントライブラリ

## エラー処理の方法

明示的なエラー処理はされていない。
APIからのレスポンスに失敗した場合、状態は更新されず、デフォルト表示のままとなる。

</Template>