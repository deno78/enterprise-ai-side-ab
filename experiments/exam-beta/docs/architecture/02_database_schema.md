# データベーススキーマ設計

## ER図

```mermaid
erDiagram
    User ||--o{ Reservation : makes
    Facility ||--o{ Reservation : has
    Reservation ||--o| Payment : has
    Reservation ||--o{ ReservationLog : tracks

    User {
        int id PK
        string username UNIQUE
        string email UNIQUE
        string password_hash
        string display_name
        string role "citizen|staff"
        string language "ja|en|zh"
        datetime created_at
        datetime updated_at
    }

    Facility {
        int id PK
        string name
        string name_en
        string name_zh
        string type "gym|meeting_room|pool"
        string address
        string address_en
        string address_zh
        int capacity
        float price_per_hour
        string description
        string description_en
        string description_zh
        string image_url
        bool is_active
        datetime created_at
    }

    Reservation {
        int id PK
        int user_id FK
        int facility_id FK
        date reserved_date
        time start_time
        time end_time
        int number_of_people
        string purpose
        string status "pending|confirmed|cancelled"
        datetime created_at
        datetime updated_at
    }

    Payment {
        int id PK
        int reservation_id FK UNIQUE
        float amount
        string method "dummy_qr"
        string qr_code_data
        string status "unpaid|paid|refunded"
        datetime paid_at
        datetime created_at
    }

    ReservationLog {
        int id PK
        int reservation_id FK
        string action "created|confirmed|cancelled|modified"
        string details
        int user_id FK
        datetime created_at
    }
```

## テーブル定義

### users
| カラム | 型 | 制約 | 説明 |
|---|---|---|---|
| id | INTEGER | PK AUTOINCREMENT | |
| username | VARCHAR(80) | UNIQUE NOT NULL | ログインID |
| email | VARCHAR(120) | UNIQUE NOT NULL | |
| password_hash | VARCHAR(256) | NOT NULL | bcrypt hash |
| display_name | VARCHAR(80) | NOT NULL | 表示名 |
| role | VARCHAR(20) | NOT NULL DEFAULT 'citizen' | citizen / staff |
| language | VARCHAR(5) | NOT NULL DEFAULT 'ja' | ja / en / zh |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | |

### facilities
| カラム | 型 | 制約 | 説明 |
|---|---|---|---|
| id | INTEGER | PK AUTOINCREMENT | |
| name | VARCHAR(200) | NOT NULL | 施設名(日本語) |
| name_en | VARCHAR(200) | | 施設名(英語) |
| name_zh | VARCHAR(200) | | 施設名(中国語) |
| type | VARCHAR(50) | NOT NULL | gym / meeting_room / pool |
| address | VARCHAR(300) | NOT NULL | 所在地(日本語) |
| address_en | VARCHAR(300) | | 所在地(英語) |
| address_zh | VARCHAR(300) | | 所在地(中国語) |
| capacity | INTEGER | NOT NULL | 収容人数 |
| price_per_hour | FLOAT | NOT NULL | 1時間あたり料金(円) |
| description | TEXT | | 説明(日本語) |
| description_en | TEXT | | 説明(英語) |
| description_zh | TEXT | | 説明(中国語) |
| image_url | VARCHAR(500) | | 画像URL |
| is_active | BOOLEAN | DEFAULT 1 | 公開フラグ |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | |

### reservations
| カラム | 型 | 制約 | 説明 |
|---|---|---|---|
| id | INTEGER | PK AUTOINCREMENT | |
| user_id | INTEGER | FK -> users.id NOT NULL | |
| facility_id | INTEGER | FK -> facilities.id NOT NULL | |
| reserved_date | DATE | NOT NULL | 予約日 |
| start_time | TIME | NOT NULL | 開始時刻 |
| end_time | TIME | NOT NULL | 終了時刻 |
| number_of_people | INTEGER | NOT NULL | 利用人数 |
| purpose | VARCHAR(500) | | 利用目的 |
| status | VARCHAR(20) | DEFAULT 'pending' | pending / confirmed / cancelled |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | |

### payments
| カラム | 型 | 制約 | 説明 |
|---|---|---|---|
| id | INTEGER | PK AUTOINCREMENT | |
| reservation_id | INTEGER | FK -> reservations.id UNIQUE NOT NULL | |
| amount | FLOAT | NOT NULL | 金額 |
| method | VARCHAR(50) | DEFAULT 'dummy_qr' | 決済方法 |
| qr_code_data | TEXT | | QRコードデータ |
| status | VARCHAR(20) | DEFAULT 'unpaid' | unpaid / paid / refunded |
| paid_at | DATETIME | | |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | |

### reservation_logs
| カラム | 型 | 制約 | 説明 |
|---|---|---|---|
| id | INTEGER | PK AUTOINCREMENT | |
| reservation_id | INTEGER | FK -> reservations.id NOT NULL | |
| action | VARCHAR(50) | NOT NULL | created / confirmed / cancelled / modified |
| details | TEXT | | 詳細 |
| user_id | INTEGER | FK -> users.id | 操作ユーザー |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | |

## インデックス

```sql
CREATE INDEX idx_reservations_user_id ON reservations(user_id);
CREATE INDEX idx_reservations_facility_id ON reservations(facility_id);
CREATE INDEX idx_reservations_date ON reservations(reserved_date);
CREATE INDEX idx_facilities_type ON facilities(type);
CREATE INDEX idx_facilities_is_active ON facilities(is_active);
```
