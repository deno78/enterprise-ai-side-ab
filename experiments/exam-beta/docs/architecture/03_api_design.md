# API 設計書

## 基本情報

- **ベースURL**: `/api`
- **プロトコル**: HTTP
- **フォーマット**: JSON (リクエスト/レスポンス)
- **認証**: セッションベース (Flask-Login)

## エラーレスポンス形式 (RFC 7807)

```json
{
  "type": "https://example.com/errors/validation-error",
  "title": "Validation Error",
  "status": 400,
  "detail": "予約日時は未来の日付を指定してください",
  "instance": "/api/reservations",
  "errors": {
    "reserved_date": "未来の日付を指定してください"
  }
}
```

## エンドポイント一覧

### 1. 認証系

#### POST /api/auth/register
ユーザー登録

**Request Body:**
```json
{
  "username": "yamada_taro",
  "email": "taro@example.com",
  "password": "SecurePass123!",
  "display_name": "山田太郎",
  "language": "ja"
}
```

**Response (201):**
```json
{
  "id": 1,
  "username": "yamada_taro",
  "email": "taro@example.com",
  "display_name": "山田太郎",
  "role": "citizen",
  "language": "ja"
}
```

#### POST /api/auth/login
ログイン

**Request Body:**
```json
{
  "username": "yamada_taro",
  "password": "SecurePass123!"
}
```

**Response (200):**
```json
{
  "message": "ログインしました",
  "user": {
    "id": 1,
    "username": "yamada_taro",
    "display_name": "山田太郎",
    "role": "citizen",
    "language": "ja"
  }
}
```

#### POST /api/auth/logout
ログアウト

**Response (200):**
```json
{ "message": "ログアウトしました" }
```

#### GET /api/auth/me
現在のユーザー情報取得

**Response (200):**
```json
{
  "id": 1,
  "username": "yamada_taro",
  "display_name": "山田太郎",
  "email": "taro@example.com",
  "role": "citizen",
  "language": "ja"
}
```

#### PUT /api/auth/profile
プロフィール更新

**Request Body:**
```json
{
  "display_name": "山田太郎(更新)",
  "language": "en"
}
```

**Response (200):**
```json
{ "message": "プロフィールを更新しました" }
```

### 2. 施設系

#### GET /api/facilities
施設一覧・検索

**Query Parameters:**
| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| q | string | 任意 | フリーワード検索 |
| type | string | 任意 | 種別絞り込み (gym/meeting_room/pool) |
| min_price | float | 任意 | 最低料金 |
| max_price | float | 任意 | 最高料金 |
| capacity | int | 任意 | 最低収容人数 |
| lang | string | 任意 | 言語 (ja/en/zh) |
| page | int | 任意 | ページ番号 (default: 1) |
| per_page | int | 任意 | 1ページ件数 (default: 20) |

**Response (200):**
```json
{
  "items": [
    {
      "id": 1,
      "name": "中央体育館",
      "type": "gym",
      "address": "東京都千代田区...",
      "capacity": 100,
      "price_per_hour": 1500,
      "image_url": "/static/images/gym.jpg",
      "is_available": true
    }
  ],
  "total": 10,
  "page": 1,
  "per_page": 20
}
```

#### GET /api/facilities/{id}
施設詳細

**Response (200):**
```json
{
  "id": 1,
  "name": "中央体育館",
  "name_en": "Central Gymnasium",
  "name_zh": "中央体育馆",
  "type": "gym",
  "address": "東京都千代田区...",
  "capacity": 100,
  "price_per_hour": 1500,
  "description": "冷暖房完備の体育館です",
  "image_url": "/static/images/gym.jpg"
}
```

#### GET /api/facilities/{id}/availability
施設の空き状況確認

**Query Parameters:**
| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| date | string | 必須 | 確認日 (YYYY-MM-DD) |

**Response (200):**
```json
{
  "facility_id": 1,
  "date": "2026-08-01",
  "slots": [
    { "time": "09:00", "available": true },
    { "time": "10:00", "available": false },
    { "time": "11:00", "available": true }
  ],
  "business_hours": { "open": "09:00", "close": "21:00" }
}
```

#### POST /api/facilities (staff only)
施設追加 (職員権限)

**Request Body:**
```json
{
  "name": "新体育館",
  "type": "gym",
  "address": "東京都新宿区...",
  "capacity": 200,
  "price_per_hour": 2000,
  "description": "新しく建設された体育館です"
}
```

#### PUT /api/facilities/{id} (staff only)
施設情報更新 (職員権限)

#### DELETE /api/facilities/{id} (staff only)
施設削除 (職員権限)

### 3. 予約系

#### GET /api/reservations
予約一覧取得

**Query Parameters:**
| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| status | string | 任意 | ステータス絞り込み |
| user_id | int | 任意 | 特定ユーザーの予約 (staff用) |

**Response (200):**
```json
{
  "items": [
    {
      "id": 1,
      "facility_name": "中央体育館",
      "reserved_date": "2026-08-01",
      "start_time": "10:00",
      "end_time": "12:00",
      "number_of_people": 10,
      "purpose": "バスケットボール練習",
      "status": "confirmed",
      "payment_status": "paid",
      "created_at": "2026-07-20T10:00:00"
    }
  ],
  "total": 5
}
```

#### POST /api/reservations
新規予約作成

**Request Body:**
```json
{
  "facility_id": 1,
  "reserved_date": "2026-08-01",
  "start_time": "10:00",
  "end_time": "12:00",
  "number_of_people": 10,
  "purpose": "バスケットボール練習"
}
```

**Response (201):**
```json
{
  "id": 1,
  "message": "予約を受け付けました",
  "amount": 3000,
  "status": "pending"
}
```

#### GET /api/reservations/{id}
予約詳細取得

#### PUT /api/reservations/{id}
予約変更

**Request Body:**
```json
{
  "reserved_date": "2026-08-02",
  "start_time": "14:00",
  "end_time": "16:00",
  "number_of_people": 8,
  "purpose": "バスケットボール練習(変更)"
}
```

#### DELETE /api/reservations/{id}
予約キャンセル

**Response (200):**
```json
{ "message": "予約をキャンセルしました" }
```

#### GET /api/reservations/{id}/pdf
予約票PDFダウンロード

**Response (200):** `application/pdf` バイナリ

### 4. 決済系

#### POST /api/payments/{reservation_id}/pay
決済実行 (ダミーQRコード生成)

**Request Body:**
```json
{
  "method": "dummy_qr"
}
```

**Response (200):**
```json
{
  "payment_id": 1,
  "amount": 3000,
  "qr_code_data": "data:image/png;base64,...",
  "status": "paid"
}
```

#### GET /api/payments/{reservation_id}
決済状況確認

**Response (200):**
```json
{
  "payment_id": 1,
  "amount": 3000,
  "status": "paid",
  "paid_at": "2026-07-20T10:30:00"
}
```

## ステータスコード一覧

| コード | 意味 |
|---|---|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request (Validation Error) |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict (重複予約など) |
| 500 | Internal Server Error |
