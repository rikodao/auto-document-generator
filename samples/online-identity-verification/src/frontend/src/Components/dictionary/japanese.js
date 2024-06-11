const defaultErrorDisplayText = require("./defaultErrorDisplayText.js");
export const japaneseLivenessDisplayText = {
  cameraMinSpecificationsHeadingText: 'カメラが最小要件を満たしていません',
  cameraMinSpecificationsMessageText: 'カメラは少なくとも320*240の解像度と15フレーム/秒をサポートする必要があります。',
  cameraNotFoundHeadingText: 'カメラにアクセスできません。',
  cameraNotFoundMessageText: 'カメラが接続されていることを確認し、他のアプリケーションがカメラを使用していないことを確認してください。カメラの権限を付与するためには設定を変更する必要があり、ブラウザのすべてのインスタンスを閉じて再試行する必要がある場合があります。',
  a11yVideoLabelText: '生体認証のためのウェブカメラ',
  cancelLivenessCheckText: '生体認証をキャンセル',
  goodFitCaptionText: '適切な位置',
  goodFitAltText: "人物の顔が楕円の中に完全に収まっている図解です。",
  hintCenterFaceText: '顔を中央に合わせる',
  hintCenterFaceInstructionText: '手順: チェックを開始する前に、カメラがスクリーンの中央上部にあり、顔がカメラの中央に来るように調整してください。チェックが開始すると、中央に楕円が表示されます。楕円の中に顔を移動させるよう促されます。その後、動かないよう促されます。数秒間動かないでいると、チェック完了の音声が聞こえるはずです。',
  hintFaceOffCenterText: '顔が楕円の中央にありません。顔をカメラの中央に合わせてください。',
  hintMoveFaceFrontOfCameraText: '顔をカメラの前に移動させる',
  hintTooManyFacesText: 'カメラの前に1つの顔のみが存在することを確認してください',
  hintFaceDetectedText: '顔が検出されました',
  hintCanNotIdentifyText: '顔をカメラの前に移動させる',
  hintTooCloseText: '距離を離す',
  hintTooFarText: '近づく',
  hintConnectingText: '接続中...',
  hintVerifyingText: '検証中...',
  hintCheckCompleteText: 'チェック完了',
  hintIlluminationTooBrightText: '暗い場所に移動する',
  hintIlluminationTooDarkText: '明るい場所に移動する',
  hintIlluminationNormalText: '照明条件は正常です',
  hintHoldFaceForFreshnessText: '動かないでください',
  hintMatchIndicatorText: '50%完了しました。さらに近づいてください。',
  photosensitivityWarningBodyText: 'このチェックでは異なる色が点滅します。光過敏の場合は注意してください。',
  photosensitivityWarningHeadingText: '光過敏に関する警告',
  photosensitivityWarningInfoText: '一部の人は、カラーライトを見ると発作を起こすことがあります。発作のリスクがある場合は注意してください。',
  photosensitivityWarningLabelText: '光過敏についての詳細情報',
  photosensitivyWarningBodyText: 'このチェックでは異なる色が点滅します。光過敏の場合は注意してください。',
  photosensitivyWarningHeadingText: '光過敏に関する警告',
  photosensitivyWarningInfoText: '一部の人は、カラーライトを見ると発作を起こすことがあります。発作のリスクがある場合は注意してください。',
  photosensitivyWarningLabelText: '光過敏についての詳細情報',
  retryCameraPermissionsText: '再試行',
  recordingIndicatorText: '録画中',
  startScreenBeginCheckText: 'ビデオチェックを開始する',
  tooFarCaptionText: '距離が遠すぎます',
  tooFarAltText: "人物の顔が楕円の中に収まっていますが、顔の輪郭と楕円の境界線に隙間があることを示した図解です。",
  waitingCameraPermissionText: 'カメラの許可を待っています。',
  ...defaultErrorDisplayText,
};