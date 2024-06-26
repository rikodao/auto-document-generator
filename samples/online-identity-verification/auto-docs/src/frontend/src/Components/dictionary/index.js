```js
## ファイル概要

このファイルは、異なる言語の表示テキストを含むオブジェクトを生成するためのモジュールです。
`english.js`、`japanese.js`、`spanish.js`モジュールをインポートしています。

## 主要なサブルーチン

このファイルには主要なサブルーチンはありません。
代わりに、`dictionary`オブジェクトを定義し、異なる言語のテキストオブジェクトを組み込んでいます。

## データ構造

`dictionary`オブジェクト: キーは言語の2文字の略語(`en`、`ja`、`es`)で、値はそれぞれの言語のテキストオブジェクトです。

## 主要なアルゴリズム

特に複雑なアルゴリズムはありません。
単に、インポートされたオブジェクトを`dictionary`オブジェクトに割り当てています。

## 入出力

入力:
- `./english.js`から`defaultLivenessDisplayText`オブジェクトをインポート
- `./japanese.js`から`japaneseLivenessDisplayText`オブジェクトをインポート
- `./spanish.js`から`spanishLivenessDisplayText`オブジェクトをインポート

出力:
- `dictionary`オブジェクトをエクスポートします。

## 利用している外部モジュールやライブラリの説明

このファイル自体は外部モジュールやライブラリを直接利用していませんが、`english.js`、`japanese.js`、`spanish.js`モジュールに依存しています。

## エラー処理の方法

特別なエラー処理は行われていません。
インポートされたモジュールが存在しない場合は、エラーが発生します。
```