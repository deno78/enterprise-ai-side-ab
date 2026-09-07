# フロントエンド構造設計

## 1. 技術選定

- **Vue.js 3** (CDN: `https://unpkg.com/vue@3/dist/vue.global.prod.js`)
- **Bootstrap 5** (CDN: `https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css`)
- **vue-i18n@9** (CDN: `https://unpkg.com/vue-i18n@9`)
- ビルド不要、シングルHTML + 分割JS構成

## 2. コンポーネントツリー

```
App.vue (ルート)
├── NavbarComponent       # ナビゲーションバー + 言語切替
├── RouterView (手動ルーティング)
│   ├── LoginPage         # ログインページ
│   ├── RegisterPage      # ユーザー登録ページ
│   ├── FacilityListPage  # 施設一覧・検索ページ
│   ├── FacilityDetailPage # 施設詳細 + 空き状況
│   ├── ReservationFormPage # 予約フォームページ
│   ├── ReservationConfirmPage # 予約確認ページ
│   ├── PaymentPage       # 決済ページ (QR表示)
│   ├── ReservationListPage # 予約一覧ページ (ユーザー)
│   ├── ReservationDetailPage # 予約詳細ページ
│   ├── ProfilePage       # プロフィール編集ページ
│   ├── AdminFacilityPage # 施設管理ページ (職員)
│   └── AdminReservationPage # 予約管理ページ (職員)
└── FooterComponent       # フッター
```

## 3. 状態管理 (Reactive Store)

グローバルな状態は Vue 3 `reactive()` で管理（Vuex不使用）。

```javascript
// store.js
const store = reactive({
  user: null,           // ログインユーザー情報
  language: 'ja',       // 現在の言語
  facilities: [],       // 施設一覧
  currentFacility: null, // 現在表示中の施設
  reservations: [],     // 予約一覧
  currentReservation: null, // 現在の予約
  searchQuery: {        // 検索条件
    q: '',
    type: '',
    min_price: null,
    max_price: null,
    capacity: null
  }
})
```

## 4. ルーティング設計

ビルド不要のため、ハッシュベースの簡易ルーターを実装:

```javascript
const routes = {
  '/': 'FacilityListPage',
  '/login': 'LoginPage',
  '/register': 'RegisterPage',
  '/facility/:id': 'FacilityDetailPage',
  '/reserve/:facilityId': 'ReservationFormPage',
  '/confirm/:reservationId': 'ReservationConfirmPage',
  '/payment/:reservationId': 'PaymentPage',
  '/reservations': 'ReservationListPage',
  '/reservations/:id': 'ReservationDetailPage',
  '/profile': 'ProfilePage',
  '/admin/facilities': 'AdminFacilityPage',
  '/admin/reservations': 'AdminReservationPage'
}
```

## 5. 多言語対応 (i18n)

### 言語ファイル構成
```javascript
const messages = {
  ja: {
    nav: { home: 'ホーム', facilities: '施設検索', reservations: '予約一覧', login: 'ログイン', register: '登録', profile: 'プロフィール', logout: 'ログアウト' },
    facility: { search: '施設検索', type: '種別', gym: '体育館', meeting_room: '会議室', pool: '温水プール', capacity: '収容人数', price: '料金', available: '空きあり', unavailable: '空きなし' },
    reservation: { title: '予約', date: '日付', start: '開始', end: '終了', people: '人数', purpose: '目的', confirm: '確認', cancel: 'キャンセル', modify: '変更' },
    payment: { title: '決済', amount: '金額', qr: 'QRコードを表示', complete: '決済完了', unpaid: '未払い' },
    common: { submit: '送信', back: '戻る', next: '次へ', download: 'ダウンロード', loading: '読み込み中...' }
  },
  en: { /* 英語訳 */ },
  zh: { /* 中国語訳 */ }
}
```

### 言語切替
- ナビゲーションバーに言語切替ドロップダウン
- 選択された言語は `localStorage` に保存
- デフォルトはブラウザ設定に連動

## 6. アクセシビリティ対応

- 全てのフォーム要素に `<label>` を付与
- 動的コンテンツには `aria-live="polite"` を設定
- キーボード操作対応 (tabindex, Enter/Space での操作)
- カラーチェック (WCAG AA 準拠)
- フォーカスインジケータの維持

## 7. ページフロー

```
ログイン → 施設検索 → 施設詳細(空き確認) → 予約フォーム
    ↓                                                    ↓
プロフィール                                          予約確認
    ↓                                                    ↓
予約一覧 ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← 決済(QR)
    ↓                                                    ↓
予約詳細 ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← PDFダウンロード
    ↓
キャンセル・変更
```

## 8. レスポンシブデザイン

- Bootstrap 5 グリッドシステム利用
- スマホ: 1カラム表示、タッチ操作最適化
- タブレット/PC: 2カラム以上のマルチカラム表示
- 施設一覧はカードレイアウト
