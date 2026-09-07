# 自治体施設予約システム 仕様書

## 1. システム概要

市民が「体育館」「会議室」「温水プール」などの自治体施設を、共通のアカウントで横断検索・予約し、最後に模擬決済と予約票（PDF）を出力するシステム。

## 2. ターゲットユーザー

### 市民ユーザー
- スマホまたはPCで施設検索する
- 検索した施設に対して予約する
- 予約票のPDFをダウンロードして、実際に施設を利用するときに見せる

### 自治体職員
- 施設管理や予約受付業務の効率化を行う
- 施設情報のメンテナンスを行う
- 施設予約状況一覧から、施設の管理者に連絡、予約状況を伝える

## 3. 機能一覧

### 3.1 ユーザー管理
- ユーザー登録（ユーザー名、メールアドレス、パスワード、表示名）
- ログイン/ログアウト（セッション管理）
- プロフィール編集（表示名、メールアドレス、言語設定）
- ロール管理（citizen / staff）

### 3.2 施設検索
- 施設名、所在地によるフリーワード検索
- 種別絞り込み（体育館 / 会議室 / 温水プール）
- 料金範囲指定
- 収容人数指定
- 多言語対応（日本語/英語/中国語）

### 3.3 予約機能
- 予約日時、人数、利用目的の入力
- 空き状況確認（時間帯ごとの空き表示）
- 予約確定（重複チェック）
- 予約変更
- 予約キャンセル

### 3.4 模擬決済
- ダミーQRコード生成
- 決済ステータス管理

### 3.5 予約票出力
- PDF形式での予約票ダウンロード
- 予約ID、施設名、日時、人数等を記載

### 3.6 管理機能（職員向け）
- 施設情報の追加・編集・削除
- 予約状況一覧表示

## 4. 技術スタック

| 項目 | 技術 |
|---|---|
| フロントエンド | Vue.js 3 (CDN) |
| CSS | Bootstrap 5 (CDN) |
| バックエンド | Python Flask 3.0 |
| データベース | SQLite (Flask-SQLAlchemy) |
| PDF生成 | ReportLab |
| QRコード | qrcode + Pillow |
| 認証 | Flask-Login + Flask-Bcrypt |
| 多言語対応 | vue-i18n (フロント)/ モデル項目 (バックエンド) |

## 5. APIエンドポイント

| メソッド | パス | 説明 |
|---|---|---|
| POST | /api/auth/register | ユーザー登録 |
| POST | /api/auth/login | ログイン |
| POST | /api/auth/logout | ログアウト |
| GET | /api/auth/me | 現在のユーザー情報 |
| PUT | /api/auth/profile | プロフィール更新 |
| GET | /api/facilities | 施設一覧/検索 |
| GET | /api/facilities/:id | 施設詳細 |
| GET | /api/facilities/:id/availability | 空き状況 |
| POST | /api/facilities | 施設追加（職員） |
| PUT | /api/facilities/:id | 施設更新（職員） |
| DELETE | /api/facilities/:id | 施設削除（職員） |
| GET | /api/reservations | 予約一覧 |
| POST | /api/reservations | 予約作成 |
| GET | /api/reservations/:id | 予約詳細 |
| PUT | /api/reservations/:id | 予約変更 |
| DELETE | /api/reservations/:id | 予約キャンセル |
| GET | /api/reservations/:id/pdf | 予約票PDF |
| POST | /api/payments/:id/pay | 決済実行 |
| GET | /api/payments/:id | 決済状況 |

## 6. データベース

- 5テーブル: users, facilities, reservations, payments, reservation_logs
- 詳細スキーマは docs/architecture/02_database_schema.md 参照

## 7. 画面一覧

| 画面 | ルート | 説明 |
|---|---|---|
| 施設一覧 | / | 検索と一覧表示 |
| 施設詳細 | /facility?id= | 詳細情報と空き状況 |
| 予約フォーム | /reserve?id= | 予約入力 |
| 決済 | /payment?id= | QRコード表示 |
| 予約一覧 | /reservations | ユーザーの予約一覧 |
| 予約詳細 | /reservation?id= | 予約内容・PDFDL・キャンセル |
| ログイン | /login | ログインフォーム |
| 登録 | /register | ユーザー登録フォーム |
| プロフィール | /profile | プロフィール編集 |
| 施設管理 | /admin/facilities | 施設CRUD（職員） |
| 予約管理 | /admin/reservations | 予約一覧（職員） |
