## ファイル概要

このファイルは、React コンポーネントとして機能し、ユーザーの顔の生体認証を行うためのインターフェースを提供しています。AWS Amplify UI React ライブラリを利用しており、特に `FaceLivenessDetector` コンポーネントを使用しています。

## 主要なサブルーチン

### `FaceLiveness`
- プロップス:
  - `faceLivenessAnalysis`: 生体認証の結果を受け取る関数
  - `sessionid`: 生体認証セッションの ID
- 状態:
  - `language`: 表示言語を管理する状態変数
- 機能:
  - 言語切り替えボタンを表示する
  - `FaceLivenessDetector` コンポーネントを表示し、生体認証を行う
  - 生体認証が完了したら `handleAnalysisComplete` 関数を呼び出す

### `handleAnalysisComplete`
- 機能:
  - 生体認証の結果を取得するためにエンドポイントに POST リクエストを送信する
  - 受け取った結果を `faceLivenessAnalysis` 関数に渡す

## データ構造

- `dictionary`: 表示テキストの多言語対応を提供するオブジェクト

## 主要なアルゴリズム

特になし

## 入出力

- 入力:
  - `sessionid`: 生体認証セッションの ID
- 出力:
  - 生体認証の結果が `faceLivenessAnalysis` 関数に渡される

## 利用している外部モジュールやライブラリの説明

- `@aws-amplify/ui-react`: AWS Amplify UI React ライブラリ
  - `ToggleButtonGroup`, `ToggleButton`: 言語切り替えボタンを表示するために使用
  - `FaceLivenessDetector`: 生体認証を行うコンポーネント
- `react`: React ライブラリ

## エラー処理の方法

- 生体認証中のエラーは `FaceLivenessDetector` コンポーネントの `onError` プロップスで処理される
- エンドポイントへのリクエストでエラーが発生した場合は、コンソールにエラーメッセージが出力される