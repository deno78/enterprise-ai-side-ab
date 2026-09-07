# 自治体施設予約システム 仕様書

## 1. システム概要

市民が「体育館」「会議室」「温水プール」などの自治体施設を、共通のアカウントで横断検索・予約し、最後に模擬決済と予約票（PDF）を出力するシステム。

## 2. ターゲットユーザー

### 市民ユーザ
- スマホまたはPCで施設検索を行う
- 検索した施設に対して予約を行う
- 予約票のPDFをダウンロードして、実際に施設を利用するときに提示する

### 自治体職員
- 施設管理や予約受付業務の効率化
- 施設情報のメンテナンス
- 施設予約状況一覧から、施設の管理者に連絡、予約状況を伝える

## 3. 機能要件

### 3.1 施設検索
- 施設名、所在地、種別（体育館、会議室、プールなど）、料金、空き状況などで検索可能

### 3.2 予約機能
- 予約日時、人数、利用目的などを入力
- 空き状況を確認し、予約確定

### 3.3 模擬決済機能
- ダミーの決済QRコードを表示する

### 3.4 予約票出力
- PDF形式で予約票を出力

### 3.5 予約確認・変更・キャンセル機能
- 予約済みの予約一覧を表示
- 予約詳細の確認
- 予約のキャンセル

### 3.6 ユーザー管理機能
- ユーザー登録、ログイン、ログアウト
- プロフィール管理（名前、メールアドレス、言語設定、パスワード変更）

## 4. 技術スタック

- フロントエンド: Vue.js 3（CDN経由）
- バックエンド: Python Flask
- データベース: SQLite
- PDF生成: fpdf2
- QRコード生成: qrcode + Pillow

## 5. システム構成

Flaskサーバがフロントエンドとバックエンドの両方を単一で稼働させる構成。

- `app.py`: メインアプリケーション（APIエンドポイント、認証、PDF生成）
- `models.py`: データベースモデル定義
- `templates/index.html`: Vue.js SPAテンプレート
- `static/css/style.css`: スタイルシート

## 6. データベース設計

### users テーブル
| カラム | 型 | 説明 |
|--------|------|------|
| id | INTEGER | 主キー |
| username | VARCHAR(80) | ユーザー名（一意） |
| email | VARCHAR(120) | メールアドレス（一意） |
| password_hash | VARCHAR(256) | パスワードハッシュ |
| name | VARCHAR(100) | 表示名 |
| lang | VARCHAR(10) | 言語設定（ja/en/zh） |
| created_at | DATETIME | 作成日時 |

### facilities テーブル
| カラム | 型 | 説明 |
|--------|------|------|
| id | INTEGER | 主キー |
| name_ja/en/zh | VARCHAR(200) | 施設名（多言語） |
| type | VARCHAR(50) | 種別（gym/meeting_room/pool） |
| location_ja/en/zh | VARCHAR(200) | 所在地（多言語） |
| price | INTEGER | 料金（円/時間） |
| capacity | INTEGER | 収容人数 |
| description_ja/en/zh | TEXT | 説明（多言語） |
| created_at | DATETIME | 作成日時 |

### reservations テーブル
| カラム | 型 | 説明 |
|--------|------|------|
| id | INTEGER | 主キー |
| user_id | INTEGER | ユーザーID（外部キー） |
| facility_id | INTEGER | 施設ID（外部キー） |
| date | DATE | 予約日 |
| start_time | VARCHAR(5) | 開始時間（HH:MM） |
| end_time | VARCHAR(5) | 終了時間（HH:MM） |
| num_people | INTEGER | 人数 |
| purpose | VARCHAR(500) | 利用目的 |
| status | VARCHAR(20) | 状態（confirmed/cancelled） |
| payment_status | VARCHAR(20) | 決済状態（unpaid/paid） |
| created_at | DATETIME | 作成日時 |

## 7. APIエンドポイント一覧

| メソッド | エンドポイント | 説明 |
|--------|------------|------|
| POST | /api/auth/register | ユーザー登録 |
| POST | /api/auth/login | ログイン |
| POST | /api/auth/logout | ログアウト |
| GET | /api/user | ユーザー情報取得 |
| PUT | /api/user | ユーザー情報更新 |
| GET | /api/facilities | 施設一覧・検索 |
| GET | /api/facilities/:id | 施設詳細 |
| GET | /api/facilities/:id/availability | 空き状況確認 |
| GET | /api/reservations | 予約一覧 |
| POST | /api/reservations | 予約作成 |
| GET | /api/reservations/:id | 予約詳細 |
| PUT | /api/reservations/:id | 予約更新 |
| DELETE | /api/reservations/:id | 予約キャンセル |
| GET | /api/reservations/:id/payment | 決済情報取得 |
| POST | /api/reservations/:id/payment | 決済実行 |
| GET | /api/reservations/:id/payment/qr | QRコード取得 |
| GET | /api/reservations/:id/pdf | 予約票PDFダウンロード |
| GET | /api/translations/:lang | 翻訳データ取得 |

## 8. UI/UX要件

- シンプルで直感的な操作性
- 多言語対応（日本語・英語・中国語） - ヘッダーのセレクトボックスで切替
- アクセシビリティ対応（適切なラベル、キーボード操作対応）
- レスポンシブデザイン（スマホ・PC対応）

## 9. 拡張性

- 施設データはデータベースで管理されており、管理画面からの追加・編集が可能な設計
- 多言語データ構造により、新言語の追加が容易
- RESTful API設計により、モバイルアプリなどからの利用も可能
