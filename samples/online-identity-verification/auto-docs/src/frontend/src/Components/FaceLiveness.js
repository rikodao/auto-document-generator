ファイルパス: /Users/naotoiso/workspace/study/auto-document-generator/samples/online-identity-verification/src/frontend/src/Components/FaceLiveness.js

```jsx
<Template>
## ファイル概要

このファイルは、顔認証ライブネス検出のためのReactコンポーネントを提供しています。
AWS Amplify UIのFaceLivenessDetectorコンポーネントを使用しており、言語の切り替えやセッション結果の取得機能があります。

## 主要なサブルーチン

- `FaceLiveness`コンポーネント
  - 引数:
    - `faceLivenessAnalysis`: セッション結果を処理するコールバック関数
    - `sessionid`: ライブネスセッションのID
  - 状態:
    - `language`: 現在選択されている言語
  - `handleAnalysisComplete`関数: ライブネスセッションの結果を取得するための非同期関数

## データ構造

- `dictionary`オブジェクト: 各言語のテキストを格納したオブジェクト

## 主要なアルゴリズム

特に複雑なアルゴリズムはありません。

## 入出力

- 入力: ライブネスセッションのID (`sessionid`プロップス)
- 出力: ライブネスセッション結果 (`handleAnalysisComplete`関数で取得)
- API エンドポイントへの POST リクエストを送信して結果を取得します。

## 利用している外部モジュールやライブラリの説明

- `@aws-amplify/ui-react`: AWS Amplify UIコンポーネントライブラリ
- `@aws-amplify/ui-react-liveness`: AWS Amplify UI Liveness Detection コンポーネント

## エラー処理の方法

- `onError`コールバックを使用してエラーをコンソールに出力します。
- API リクエストの失敗時はエラーが発生する可能性があります。

</Template>
```