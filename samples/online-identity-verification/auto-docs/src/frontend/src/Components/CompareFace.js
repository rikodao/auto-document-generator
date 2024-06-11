<Template>
## ファイル概要

このファイルは、ReactコンポーネントであるCompareFaceResultを定義しています。このコンポーネントは、IDイメージとライブネス分析イメージを比較し、その類似性スコアを表示する機能を持っています。
関連するモジュールやパッケージは、react、@aws-amplify/ui-reactがインポートされています。

## 主要なサブルーチン

- `checkSimilarity`
  - 引数: なし
  - 戻り値: なし
  - グローバル変数の使用: `endpoint`, `sessionid`
  - 機能: APIエンドポイントに対してGETリクエストを送信し、IDイメージとライブネス分析イメージの類似性スコアと、IDイメージの顔部分の切り抜き画像のURLを取得します。取得した値を状態変数に格納します。

- `resultComponet`
  - 引数: `similarityScore`
  - 戻り値: JSXの要素
  - グローバル変数の使用: `croppedImageUrl`
  - 機能: 類似性スコアと切り抜き画像のURLを受け取り、それらを表示するJSXの要素を返します。

- `checkComponet`
  - 引数: なし
  - 戻り値: JSXの要素
  - グローバル変数の使用: `idImage`, `faceLivenessAnalysis`
  - 機能: IDイメージとライブネス分析イメージを表示し、類似性スコアをチェックするためのボタンを表示するJSXの要素を返します。

## データ構造

- `similarityScore`: 状態変数、IDイメージとライブネス分析イメージの類似性スコアを格納します。
- `croppedImageUrl`: 状態変数、IDイメージの顔部分の切り抜き画像のURLを格納します。
- `checking`: 状態変数、類似性スコアのチェック中かどうかを示すブール値を格納します。

## 主要なアルゴリズム

特に複雑なアルゴリズムは使用されていません。

## 入出力

- 入力: `idImage` (IDイメージのURL), `faceLivenessAnalysis` (ライブネス分析イメージのBase64エンコードされたデータ), `sessionid` (セッションID)
- 出力: IDイメージとライブネス分析イメージの類似性スコアと、IDイメージの顔部分の切り抜き画像を表示するコンポーネント
- 外部モジュールの利用: fetch APIを使用してAPIエンドポイントに対してGETリクエストを送信しています。

## 利用している外部モジュールやライブラリの説明

- `react`: Reactライブラリ
- `@aws-amplify/ui-react`: AWS Amplify UIコンポーネントライブラリ

## エラー処理の方法

特別なエラー処理は実装されていません。

</Template>