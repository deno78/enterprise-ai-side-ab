---
marp: true
theme: default
size: 16:9
paginate: true
header: "📼 MIXTAPE : ENTERPRISE AI DEV [SIDE A & B]"
footer: "H協システム開発部会 2026 | Matsusaka E.D.P. Center Co., Ltd."
style: |
  @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Zen+Kaku+Gothic+New:wght@500;700;900&display=swap');

  section {
    font-family: 'Zen Kaku Gothic New', 'Segoe UI', 'Meiryo', sans-serif;
    font-size: 22px;
    padding: 42px 55px 35px 55px;
    background-color: #f7f4ed;
    color: #2b2b2b;
    position: relative;
    box-sizing: border-box;
    background-image: 
      linear-gradient(to right, rgba(0,0,0,0.03) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(0,0,0,0.03) 1px, transparent 1px);
    background-size: 24px 24px;
  }

  /* カセットテープの外枠シェル装飾 */
  section::before {
    content: "";
    position: absolute;
    top: 10px; left: 10px; right: 10px; bottom: 10px;
    border: 3px solid #2d3139;
    border-radius: 10px;
    pointer-events: none;
  }

  /* ヘッダー・フッターのカセットデッキ風装飾 */
  header {
    font-family: 'Share Tech Mono', 'Courier New', monospace;
    font-size: 14px;
    color: #555c66;
    font-weight: bold;
    letter-spacing: 1.5px;
    border-bottom: 2px solid #333842;
    padding-bottom: 4px;
    top: 20px;
    left: 55px;
    right: 55px;
  }
  footer {
    font-family: 'Share Tech Mono', 'Courier New', monospace;
    font-size: 13px;
    color: #6c757d;
    border-top: 1px dashed #2d3139;
    padding-top: 4px;
    bottom: 20px;
    left: 55px;
    right: 55px;
  }

  /* 見出しデザイン */
  h1 {
    font-family: 'Zen Kaku Gothic New', sans-serif;
    font-weight: 900;
    font-size: 32px;
    color: #1a1c20;
    margin-top: 0;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  h2 {
    font-size: 22px;
    font-weight: 700;
    color: #454d55;
    margin-top: 0;
    margin-bottom: 14px;
  }
  h3 {
    font-size: 20px;
    color: #222;
    margin: 10px 0 6px 0;
  }

  /* A面・B面のカラーアクセント */
  .side-a-title h1, .theme-a h1 {
    color: #b71c1c;
    border-left: 8px solid #b71c1c;
    padding-left: 12px;
  }
  .side-b-title h1, .theme-b h1 {
    color: #1b5e20;
    border-left: 8px solid #1b5e20;
    padding-left: 12px;
  }

  /* カセットテープUIバッジ */
  .badge {
    display: inline-block;
    font-family: 'Share Tech Mono', monospace;
    font-size: 14px;
    font-weight: bold;
    padding: 2px 10px;
    border-radius: 4px;
    letter-spacing: 1px;
    vertical-align: middle;
  }
  .badge-a {
    background-color: #b71c1c;
    color: #ffffff;
    box-shadow: 2px 2px 0px #600;
  }
  .badge-b {
    background-color: #1b5e20;
    color: #ffffff;
    box-shadow: 2px 2px 0px #040;
  }
  .badge-gold {
    background-color: #c59b27;
    color: #111;
    font-weight: 900;
  }
  .badge-dark {
    background-color: #23272e;
    color: #00e676;
    border: 1px solid #444;
  }
  .counter {
    font-family: 'Share Tech Mono', monospace;
    background-color: #111;
    color: #ffb300;
    padding: 2px 8px;
    border-radius: 3px;
    border: 1px solid #444;
    font-size: 15px;
    letter-spacing: 2px;
  }

  /* ボックスデザイン（カセットレーベル/メモ風） */
  .point-box {
    background-color: #ffffff;
    border: 2px solid #2d3139;
    border-left: 10px solid #c59b27;
    padding: 12px 18px;
    margin: 12px 0;
    box-shadow: 3px 3px 0px rgba(0,0,0,0.15);
    border-radius: 0 6px 6px 0;
  }
  .ng-box {
    background-color: #fff4f2;
    border: 2px solid #b71c1c;
    border-left: 10px solid #b71c1c;
    padding: 10px 16px;
    margin: 10px 0;
    box-shadow: 3px 3px 0px rgba(183,28,28,0.2);
    border-radius: 0 6px 6px 0;
  }
  .ok-box {
    background-color: #f1f8f3;
    border: 2px solid #1b5e20;
    border-left: 10px solid #1b5e20;
    padding: 10px 16px;
    margin: 10px 0;
    box-shadow: 3px 3px 0px rgba(27,94,32,0.2);
    border-radius: 0 6px 6px 0;
  }

  /* テーブル（カセットスペック表／トラックリスト風） */
  table {
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    font-size: 16px;
    margin: 10px 0;
    background-color: #ffffff;
    box-shadow: 3px 3px 0px rgba(0,0,0,0.12);
    border: 2px solid #2d3139;
  }
  th {
    background-color: #2d3139;
    color: #f7f4ed;
    font-family: 'Zen Kaku Gothic New', sans-serif;
    font-weight: 700;
    padding: 8px 14px;
    text-align: left;
    border: 1px solid #454d55;
  }
  td {
    padding: 8px 14px;
    border: 1px solid #dcd7cc;
    vertical-align: middle;
    line-height: 1.4;
  }
  tr:nth-child(even) td {
    background-color: #fcfbfa;
  }

  /* コードブロック（カセットデッキのディスプレイ・ターミナル風） */
  pre {
    background-color: #1a1c22 !important;
    border: 2px solid #333842;
    border-radius: 6px;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.8), 3px 3px 0px rgba(0,0,0,0.2);
    padding: 12px 18px !important;
  }
  pre code {
    font-family: 'Share Tech Mono', 'Consolas', monospace !important;
    color: #4af626 !important;
    font-size: 17px !important;
    line-height: 1.4 !important;
    background: transparent !important;
  }
  code {
    font-family: 'Share Tech Mono', 'Consolas', monospace;
    background-color: #e9e4d8;
    color: #c2185b;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.9em;
  }

  /* 表紙用スタイル */
  section.cover {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 60px 80px;
  }
  section.cover h1 {
    font-size: 44px;
    color: #1a1c20;
    margin-top: 15px;
    margin-bottom: 12px;
    border-left: none;
    padding-left: 0;
    line-height: 1.2;
  }
  section.cover h2 {
    font-size: 24px;
    color: #555c66;
    font-weight: 700;
    margin-top: 0;
    margin-bottom: 30px;
  }
  section.cover header, section.cover footer {
    display: none;
  }

  /* B面への反転スライド */
  section.reverse {
    background: #14171a;
    color: #ffffff;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  section.reverse::before {
    border: 3px solid #ff9800;
  }

  /* 終了スライド */
  section.outro {
    background: #1a1c22;
    color: #f7f4ed;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.outro::before {
    border: 3px solid #c59b27;
  }
---

<!-- _class: cover -->
<!-- _paginate: false -->

<div>
  <div style="display: flex; gap: 12px; align-items: center;">
    <span class="badge badge-a" style="font-size: 16px; padding: 4px 14px;">SIDE A</span>
    <span class="badge badge-b" style="font-size: 16px; padding: 4px 14px;">SIDE B</span>
    <span class="badge badge-gold" style="font-size: 15px;">C-60</span>
    <span style="font-family: 'Share Tech Mono'; color: #666; font-size: 15px; margin-left: 8px;">HIGH POSITION [TYPE II]</span>
  </div>

  <h1>エンタープライズAI開発のA面／B面</h1>
  <h2>実証実験止まりを脱却する「分業」と「境界設計」</h2>

  <div style="margin-top: 40px; border-top: 2px solid #2d3139; padding-top: 20px; display: flex; justify-content: space-between; align-items: flex-end;">
    <div>
      <div style="font-family: 'Share Tech Mono'; color: #b71c1c; font-weight: bold; font-size: 16px; margin-bottom: 4px; letter-spacing: 1px;">★ H協 システム開発部会 2026 ★</div>
      <div style="font-size: 20px; font-weight: 700; color: #2b2b2b;">第2回部会 講演資料</div>
    </div>
    <div style="text-align: right; font-family: 'Share Tech Mono'; color: #555; font-size: 15px; line-height: 1.6;">
      <div>DATE: 2026.09.17</div>
    </div>
  </div>
</div>

---

# 📼 はじめに

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="counter">INDEX 00</span>
  <span style="font-family: 'Share Tech Mono'; color: #666; font-size: 15px;">PLAYBACK MODE: CONTINUOUS</span>
</div>

### 🎯 今日お話しすること
- AIを使って、ある程度以上の規模・ **エンタープライズでの開発** をやりたい。
- 単なるPoC（実証実験）止まりではなく、 **現場で動くシステム・製品** を作りたい。
- 「バイブコーディングでは属人的で再現性がない」と感じている。

### 🚫 話さないこと
- Gemini？ Claude？ OpenAI？ DeepSeek？ どれが最強モデルか？
  （※モデル自体の優劣ではなく、 **「AIをどう使いこなすか」の設計論** に焦点を当てます）
- 既存プロダクトにAIをどう組み込むか？（主に開発方法論について話します）

<div class="point-box">
<b>💡 本日のコアメッセージ：</b><br>
<b>「内部：組織・体制（A面）」</b>と<b>「外部：境界（B面）」</b>の2面が揃って初めてAI開発は成立する！
</div>

---

# 📑 INDEX

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="counter">INDEX 01</span>
  <span class="badge badge-dark">▶ 2 TRACKS TOTAL : 45 MIN</span>
</div>


- ### 🔴 **TRACK 01 【A面】エージェンティックAI（組織・体制論）**
  - なぜバイブコーディングは破綻するのか？
  - 分業（エージェント）＋ 規約（スキル）＋ 仕様書駆動の実証比較

- ### 🟢 **TRACK 02 【B面】境界設計（システム・アーキテクチャ論）**
  - なぜ直接Excelや画像を作らせると失敗するのか？
  - 入力（MCP/Graphify）・出力（中間データ）・実行（IDE/CLI）の境界

---

<!-- 
=====================================================
  PART 1: A面 エージェンティックAI（組織・体制論）
=====================================================
-->

<!-- _class: side-a-title -->

# <span class="badge badge-a" style="font-size: 24px;">SIDE A</span> エージェンティックAI
## 〜 1人のAIに丸投げするのをやめ、チームで開発する 〜

<div style="margin-top: 40px; display: flex; gap: 30px; align-items: center;">
  <div style="flex: 1; background: #fff0f0; border: 2px solid #b71c1c; padding: 20px; border-radius: 8px; box-shadow: 4px 4px 0 rgba(183,28,28,0.2);">
    <div style="font-family: 'Share Tech Mono'; color: #b71c1c; font-weight: bold; font-size: 16px;">▶ SIDE A : FOCUS</div>
    <h3 style="color: #b71c1c; margin-top: 5px;">「誰が・どういう役割で・どんな規約で」</h3>
    <p style="font-size: 18px; margin: 0; color: #444;">
      単一プロンプトへの丸投げから脱却し、専門エージェントの分業体制を組む組織論。
    </p>
  </div>
  <div style="flex: 1; text-align: center;">
    <div style="font-family: 'Share Tech Mono'; font-size: 40px; color: #b71c1c; font-weight: bold;">▶ PLAYING</div>
    <div style="font-family: 'Share Tech Mono'; font-size: 16px; color: #666; letter-spacing: 2px;">TRACK 01 / TOTAL 20 MIN</div>
    <div style="font-family: 'Share Tech Mono'; font-size: 14px; color: #888; margin-top: 10px;">EQ: NORMAL BIAS [120µs]</div>
  </div>
</div>

---

<div class="theme-a">

# みなさん、こういう経験ありませんか？

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
  <span class="badge badge-a">SIDE A : ISSUE</span>
  <span class="counter">TRACK 01-1</span>
</div>

- チャットを長く続けていると、 **段々アホになる・指示を忘れる** 。
- 短い関数を書かせると凄いのに、 **大規模になると途端に雑になる** 。
- バイブコーディングしていると、急に手抜きをしたり早く切り上げようとする。
- **「ぶっちゃけ、エンタープライズの現場開発には使えないのでは…？」**

<div class="ng-box">
<b>⚠ AIは賢いのか？バカなのか？</b><br>
最初は天才プログラマーに見えたAIが、会話が進むにつれて動かないコードを量産し始める！！
</div>

</div>

---

<div class="theme-a">

# バイブコーディングで何が起きているか？

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
  <span class="badge badge-a">SIDE A : MECHANISM</span>
  <span class="counter">TRACK 01-2</span>
</div>

1. **「更新ボタン付けて！」** ➔ 「付けました！」（元気いっぱい！）
2. **「削除ボタン付けて！」** ➔ 「付けました！」（1の内容と履歴を読んで…）
3. **「編集ボタン付けて！」** ➔ 「付けました！」（1, 2の内容と履歴を読んで…）
99. **「〇〇ボタン付けて！」** ➔ 「付けました！」なんかおかしくなってくる…


### 発生する致命的な問題
- 実装パターンがボタンごとにバラバラになる。
- 1つのモジュールが肥大化してスパゲッティコードになる。
- チャット履歴が増えるほど記憶容量を圧迫し、**最初の前提や設計規約を忘れていく** 。

</div>

---

<div class="theme-a">

# 原因：LLMの「コンテキスト限界」

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="badge badge-a">SIDE A : ROOT CAUSE</span>
  <span class="counter">TRACK 01-3</span>
</div>

- LLMには **コンテキスト量（一度に扱える情報量）** という性能限界がある。
- まるで **「人間の記憶領域」** のように、容量が満杯になると上書きや忘却が起こる。

<div style="background: #1e2025; border: 2px solid #333842; border-radius: 8px; padding: 16px 20px; margin: 12px 0; color: #fff;">
  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; font-family: 'Share Tech Mono', sans-serif;">
    <span style="width: 210px; font-weight: bold; color: #81c784; font-size: 16px;">🟢 初期（残量十分）</span>
    <div style="flex: 1; height: 16px; background: #333; border-radius: 4px; overflow: hidden; margin: 0 15px;">
      <div style="width: 25%; height: 100%; background: #4caf50;"></div>
    </div>
    <span style="width: 310px; font-size: 15px; color: #ccc;">クリアな推論・丁寧な実装</span>
  </div>
  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; font-family: 'Share Tech Mono', sans-serif;">
    <span style="width: 210px; font-weight: bold; color: #ffb74d; font-size: 16px;">🟡 中期（残量半分）</span>
    <div style="flex: 1; height: 16px; background: #333; border-radius: 4px; overflow: hidden; margin: 0 15px;">
      <div style="width: 65%; height: 100%; background: #ff9800;"></div>
    </div>
    <span style="width: 310px; font-size: 15px; color: #ccc;">ハルシネーション混入・ニュアンスの欠落</span>
  </div>
  <div style="display: flex; align-items: center; justify-content: space-between; font-family: 'Share Tech Mono', sans-serif;">
    <span style="width: 210px; font-weight: bold; color: #e57373; font-size: 16px;">🔴 後期（残量限界）</span>
    <div style="flex: 1; height: 16px; background: #333; border-radius: 4px; overflow: hidden; margin: 0 15px;">
      <div style="width: 100%; height: 100%; background: #f44336;"></div>
    </div>
    <span style="width: 310px; font-size: 15px; color: #ff8a80; font-weight: bold;">フリーズ・重要な規約忘却！</span>
  </div>
</div>

<div class="ng-box">
<b>❌ コンテキストが溢れると、AIは過去の情報を圧縮・忘却し、精度が急降下する！</b>
</div>

</div>

---

<div class="theme-a">

# 解決策：1人に任せず「分業」させる

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="badge badge-a">SIDE A : SOLUTION</span>
  <span class="counter">TRACK 01-4</span>
</div>

<div class="point-box">
<b>💡 エージェンティックAIの考え方：</b><br>
1人の天才に全工程を丸投げするのではなく、<b>「専門エージェント」と「スキル（規約）」</b>を定義して組織的に開発させる。
</div>

### 役割分担（マルチエージェント体制）
- 📐 **アーキテクト（設計担当）** ：全体構造・インターフェース・データ構造を設計
  - フロントエンドUI/UX設計
  - バックエンド,DB設計
- 💻 **デベロッパー（実装担当）** ：設計書に基づいてモジュール単位でクリーン実装
- 🔍 **レビュアー（品質担当）** ：コーディング規約やチェックリストに沿って厳格検証

</div>

---

<div class="theme-a">

# 検証：施設予約システムを作らせてみた

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="badge badge-a">SIDE A : EXPERIMENT</span>
  <span class="counter">TRACK 01-5</span>
</div>

同じ概要設計書から、2つの手法でシステムを生成・比較検証を実施。

- **alpha（単一AIに丸投げ）** ：概要設計書をそのままチャットに渡して一発生成
- **beta（組織を定義して分業）** ：役割（エージェント）と規約（スキル）を設定してから生成

### 🎛 試験環境スペック
- **AIツール** ：OpenCode
- **使用LLM** ：Google Gemini 3.8 Flash Lite
- **要件** ：施設検索・予約・模擬決済・PDF出力・多言語対応・管理画面

</div>

---

<div class="theme-a">

# 入力ファイルの例

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="badge badge-a">SIDE A : EXPERIMENT</span>
  <span class="counter">TRACK 01-6</span>
</div>

### システム概要: 
  - 市民が「体育館」「会議室」などの施設を、検索・予約し、最後に予約票を出力するシステム。
### 機能要件
  - 施設検索: 施設名、種別（体育館、会議室）、料金、空き状況などで検索可能
  - 予約機能: 予約日時、人数、利用目的などを入力、空き状況を確認し、予約確定
### 技術スタック
  - フロントエンド: Vue.js(CDN経由)
  - バックエンド: Python Flask
### UI/UX要件
  - 多言語対応（日本語・英語・中国語）

</div>

---

<div class="theme-a">

# 比較結果：設計・コード品質

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
  <span class="badge badge-a">SIDE A : BENCHMARK</span>
  <span class="counter">TRACK 01-7</span>
</div>

## alpha（単一丸投げ）
- **アーキテクチャ** : モノリシック（1ファイルに全集中） 
- **Python品質** : 可読性はあるがエラー処理が粗い 
- **JS/フロント品質** : 単一HTMLに690行ベタ書き 
- **多言語対応** : 辞書の重複・保守破綻あり

## beta（組織を定義して分業）
-  **アーキテクチャ** : **モジュール分割（Blueprint設計）**
-  **Python品質** : **堅牢・構造化・バリデーション充実**
-  **JS/フロント品質** : **13コンポーネント分割、SPA構成**
-  **多言語対応** : **vue-i18n で適切に分離管理**

<div class="ok-box" style="margin-top: 6px; padding: 6px 14px;">
<b>✅ エージェント分業により、コードのモジュール性・保守性が劇的に向上！</b>
</div>
</div>

---

<div class="theme-a">

# A面の結論：これって我々の仕事そのものでは？

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="badge badge-a">SIDE A : CONCLUSION</span>
  <span class="counter">TRACK 01-8</span>
</div>

<div class="point-box">
<b>我々が何十年もやってきた「システムエンジニアリング（組織・規約）」そのもの！</b>
</div>

- **1人の新人に全工程投げたら炎上**
  ➔ 単一プロンプトへの丸投げでコード崩壊
- **役割分担（設計・開発・テスト）**
  ➔ エージェント分業（Architect / Dev / Reviewer）
- **社内開発標準・チェックリスト**
  ➔ スキル（ルールファイル・規約の注入）
- **仕様書ベースの進捗・受け渡し**
  ➔ 仕様書駆動（中間ドキュメントによる連携）

</div>

---

<!-- 
=====================================================
  INTERLUDE: B面への裏返し（AUTO REVERSE）
=====================================================
-->

<!-- _class: reverse -->
<!-- _paginate: false -->

<div style="width: 900px; padding: 30px; border: 3px dashed #ff9800; border-radius: 16px; background: rgba(0,0,0,0.6);">
  <div style="font-family: 'Share Tech Mono'; font-size: 24px; color: #ff9800; letter-spacing: 4px; margin-bottom: 15px;">
    🔄 AUTO REVERSE / TURN OVER
  </div>
  <h1 style="font-size: 46px; color: #ffffff; margin: 15px 0; justify-content: center; border: none;">
    カセットテープを裏返します
  </h1>
  <div style="font-size: 24px; color: #a5d6a7; font-weight: bold; margin: 15px 0;">
    【A面：組織・体制論】から【B面：システム・アーキテクチャ論】へ
  </div>
  <div style="display: flex; justify-content: center; gap: 20px; margin-top: 25px;">
    <span class="badge badge-dark" style="font-size: 18px; padding: 6px 16px;">SIDE A : FINISHED</span>
    <span class="badge badge-b" style="font-size: 18px; padding: 6px 16px;">▶ SIDE B : READY TO PLAY</span>
  </div>
</div>

---

<!-- 
=====================================================
  PART 2: B面 境界設計（アーキテクチャ論）
=====================================================
-->

<!-- _class: side-b-title -->

# <span class="badge badge-b" style="font-size: 24px;">SIDE B</span> 境界設計
## 〜 AIに「何をやらせ、何を外部に任せるか」 〜

<div style="margin-top: 40px; display: flex; gap: 30px; align-items: center;">
  <div style="flex: 1; background: #f1f8f3; border: 2px solid #1b5e20; padding: 20px; border-radius: 8px; box-shadow: 4px 4px 0 rgba(27,94,32,0.2);">
    <div style="font-family: 'Share Tech Mono'; color: #1b5e20; font-weight: bold; font-size: 16px;">▶ SIDE B : FOCUS</div>
    <h3 style="color: #1b5e20; margin-top: 5px;">「入出力と実行環境のインターフェース」</h3>
    <p style="font-size: 18px; margin: 0; color: #444;">
      組織を作っても環境を誤ると失敗する。LLMを正しく推論エンジンとして組み込む境界論。
    </p>
  </div>
  <div style="flex: 1; text-align: center;">
    <div style="font-family: 'Share Tech Mono'; font-size: 40px; color: #1b5e20; font-weight: bold;">▶ PLAYING</div>
    <div style="font-family: 'Share Tech Mono'; font-size: 16px; color: #666; letter-spacing: 2px;">TRACK 02 / TOTAL 20 MIN</div>
    <div style="font-family: 'Share Tech Mono'; font-size: 14px; color: #888; margin-top: 10px;">EQ: HIGH BIAS [70µs]</div>
  </div>
</div>

---

<div class="theme-b">

# B面の課題：なぜAIはうまくファイルを出力できないのか？

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="badge badge-b">SIDE B : ISSUE</span>
  <span class="counter">TRACK 02-1</span>
</div>

**「AIへの入出力や実行環境」** を誤ると失敗します。

<div class="ng-box">
<b>❌ よくある現場の事例（BAD INPUT/OUTPUT）：</b><br>
・「この要件でいい感じのExcel設計書（.xlsx）を作って！」<br>
・「画面デザインの完成画像をピクセル単位で一発生成して！」<br>
・「分厚い設計書PDFを生のままプロンプトに貼るから読んで！」<br>
・「大量のソースコードに含まれる関数呼び出しを調べて！」
</div>

### なぜうまくいかないのか？
LLMは「万能アプリ」ではなく、 **「テキスト推論エンジン」** だからです。

</div>

---

<div class="theme-b">

# 成功のための「3つの境界設計」

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
  <span class="badge badge-b">SIDE B : CORE MODEL</span>
  <span class="counter">TRACK 02-2</span>
</div>

<div style="display: grid; grid-template-columns: 1fr 1.15fr 1fr; gap: 14px; align-items: stretch; margin-top: 10px;">
  <!-- 入力の境界 -->
  <div style="background: #ffffff; border: 2px solid #1565c0; border-radius: 8px; padding: 12px 14px; box-shadow: 3px 3px 0 rgba(21,101,192,0.15);">
    <span class="badge badge-a" style="background:#1565c0; color:#fff; font-size:12px; margin-bottom:6px;">【入力の境界】</span>
    <div style="font-weight: bold; font-size: 17px; color: #1565c0; margin-bottom: 4px;">生データを構造化</div>
    <p style="font-size: 14px; color: #444; margin: 0; line-height: 1.4;">巨大PDFや生コードを丸投げせず、<b>MCP / Graphify</b> で必要な文脈だけを抽出して渡す</p>
  </div>

  <!-- 思考のコア -->
  <div style="background: #fff8f8; border: 2px solid #b71c1c; border-radius: 8px; padding: 12px 14px; box-shadow: 3px 3px 0 rgba(183,28,28,0.15); text-align: center;">
    <span class="badge badge-b" style="font-size:12px; margin-bottom:6px;">思考のコア (LLM)</span>
    <div style="font-weight: 900; font-size: 18px; color: #b71c1c; margin-bottom: 4px;">意味理解 ＆ 論理的推論</div>
    <p style="font-size: 14px; color: #444; margin: 0; line-height: 1.4;">要件分析・アーキテクチャ検討・コード生成など「頭脳ワーク」に集中させる</p>
  </div>

  <!-- 出力の境界 -->
  <div style="background: #ffffff; border: 2px solid #2e7d32; border-radius: 8px; padding: 12px 14px; box-shadow: 3px 3px 0 rgba(46,125,50,0.15);">
    <span class="badge badge-a" style="font-size:12px; margin-bottom:6px;">【出力の境界】</span>
    <div style="font-weight: bold; font-size: 17px; color: #2e7d32; margin-bottom: 4px;">中間データを出力</div>
    <p style="font-size: 14px; color: #444; margin: 0; line-height: 1.4;">直接バイナリを作らせず、<b>JSON / Markdown</b> を出力させスクリプトで変換する</p>
  </div>
</div>

<!-- 実行の境界 -->
<div style="background: #f3f9fc; border: 2px solid #0277bd; border-radius: 8px; padding: 10px 18px; margin-top: 12px; box-shadow: 3px 3px 0 rgba(2,119,189,0.15); display: flex; justify-content: space-between; align-items: center;">
  <div>
    <span class="badge badge-b" style="background:#0277bd; color:#fff; font-size:12px; margin-right: 8px;">【実行の境界】</span>
    <b style="font-size: 16px; color: #01579b;">AIに手足（IDE / CLI）を与える</b>
  </div>
  <span style="font-size: 14px; color: #333;">ファイル直接編集 ➔ 自動テスト ➔ エラー自己修復ループを回す</span>
</div>

</div>

---

<div class="theme-b">

# 境界1：出力の境界設計
## 〜 いきなりExcelや画像を作らせるのはNG 〜

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="badge badge-b">SIDE B : OUTPUT</span>
  <span class="counter">TRACK 02-3</span>
</div>

### なぜ直接 `.xlsx` や完成画像を作らせるとダメなのか？
- **バイナリ・ピクセル計算の不得意さ** ：セル座標のズレ、計算式の破損
- **検証不能** ：出力が正しいか自動テスト・CIで検証できない
- **再現性ゼロ** ：微修正を頼むと、関係ない部分のデザインまで崩れる

<div class="point-box">
LLMに<b>「ピクセル描画」や「バイナリ構築」</b>をやらせてはいけない！
</div>

</div>

---

<div class="theme-b">

# 出力境界の正解：中間データ ＋ プログラム

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
  <span class="badge badge-b">SIDE B : PIPELINE</span>
  <span class="counter">TRACK 02-4</span>
</div>

### 3段階の出力パイプライン（境界の分離）

1. **AI (LLM) 【非決定論的領域】**
   - 意味理解・論理的推論、非構造化データからの情報抽出
   - 直接バイナリを作らせず、 **「構造化テキスト」** の生成に専念させる

2. **中間データ（JSON / YAML / Markdown） 【品質の防波堤】**
   - Gitによるテキスト差分管理（レビュー可能性の確保）
   - JSONスキーマ検証・自動テスト（CI/CD）による機械的品質チェック

3. **最終成果物（.xlsx / .pdf / .pptx） 【決定論的領域】**
   - Python (`openpyxl` 等) や Marp 等の決定論的プログラム・テンプレートで出力

<div class="ok-box">
<b>✅ </b> AIには<b>「構造化テキスト」</b>を作らせ、バイナリ変換は<b>「決定論的スクリプト」</b>に任せる！
</div>

</div>

---

<div class="theme-b">

# 中間データ方式の圧倒的メリット

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
  <span class="badge badge-b">SIDE B : BENEFIT</span>
  <span class="counter">TRACK 02-5</span>
</div>

## AIに直接作らせる
- **再現性** : 低い（毎回レイアウトが変わる）
- **品質検証** : 人間が全セルを目視確認
- **バージョン管理** : バイナリは差分（diff）不可
- **修正の容易さ** : 指示するたびに全体が壊れる

## 中間データ ＋ スクリプト
- **再現性** : 100%（テンプレートで完全固定）
- **品質検証** : JSONスキーマや自動テストで瞬時に検証
- **バージョン管理** : Gitでテキスト差分が完全に追える
- **修正の容易さ** : 対象のJSONキーやスクリプトのみ修正

> 📼 **身近な例** ：本スライドも **Marp（Markdown）** という中間データを経由して生成しています！

</div>

---

<div class="theme-b">

# 境界2：入力の境界設計
## 〜 AIが読みやすい形（MCP / Graphify）に変換する 〜

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="badge badge-b">SIDE B : INPUT</span>
  <span class="counter">TRACK 02-6</span>
</div>

### 生データをそのまま丸投げする問題点
- 巨大な設計書PDFや数千ファイルのソースコードを丸ごとプロンプトに貼ると…
  - **トークン上限の圧迫** （コスト高 ＆ 忘却）
  - **ノイズによるハルシネーション** （関係ない情報に引っ張られる）
- 全文を読むのを諦めて、Grepで検索して必要なファイルやコードだけを探そうとする。
- そもそもExcelやWordを直接読めない…。

<div class="point-box">
<b>💡 入力の境界設計：</b><br>
AIが理解しやすいように、<b>事前に構造化・抽象化して必要な情報だけをオンデマンドで渡す</b>。
</div>

</div>

---

<div class="theme-b">

# 入力境界の武器：MCP と Graphify

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="badge badge-b">SIDE B : TOOLS</span>
  <span class="counter">TRACK 02-7</span>
</div>

### 1. 🔌 MCP (Model Context Protocol)
- AIと外部データ（DB、Git、Slack、社内API）を繋ぐオープン標準。
- **「全量投入」ではなく「必要な時にツール経由でオンデマンド取得」** する。

### 2. 🕸 Graphify / AST（構文木）解析
- ソースコードや文書の依存関係を **ナレッジグラフ** として事前抽出。
- 「影響範囲のあるモジュール一覧」だけをAIに渡すことで、最小限のトークンで全体像を把握させる。

### 3. 📚 Pandoc / テキスト変換
- WordやExcel,PDFなどをテキスト形式（markdown,json,text）変換。

<div class="ok-box">
<b>💡 入力の境界設計：</b><br>
データを効果的に読み出せるように、AIフレンドリーな入力形態を用意しておく。
</div>

</div>

---

<div class="theme-b">

# 境界3：実行の境界設計
## 〜 AIに手足（IDE / CLI）を用意する 〜

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="badge badge-b">SIDE B : RUNTIME</span>
  <span class="counter">TRACK 02-8</span>
</div>

### Webチャット画面の限界
- AIがコード出力 ➔ 人間がコピペ ➔ エラー発生 ➔ 人間がエラーをAIにコピペ…
- ➔ **人間が単なる「コピペの伝書鳩」になって疲弊する！**

<div class="point-box">
<b>💡 実行の境界設計：</b><br>
AIに<b>ファイル操作・コマンド実行・テスト実行ができる「環境（手足）」</b>を与える。
</div>

</div>

---

<div class="theme-b">

# 手足を持つAI環境と自律フィードバックループ

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="badge badge-b">SIDE B : FEEDBACK LOOP</span>
  <span class="counter">TRACK 02-9</span>
</div>

### 現代のAI開発環境（手足の提供）
- **AI統合IDE** ：Cursor, VS Code & Cline/Copilot, Antigravity
- **自律型CLI** ：Aider, Claude Code, OpenCode
    - Plan[1. 計画立案]
      - Edit[2. ファイル直接編集] && Run[3. テスト/ビルド実行]
      - Check[4. エラー判定]  
        - OK --> [5. Done] 
        - NG --> [2. Edit]
    - Done[5. 完了・レビュー依頼]

- AIが自ら **「修正 ➔ テスト ➔ エラーログ確認 ➔ 再修正」** のループを回す！

</div>

---

<!-- 
=====================================================
  PART 3: 全体統合・まとめ
=====================================================
-->

# 🎛 A面とB面の統合アーキテクチャ

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
  <span class="badge badge-gold">INTEGRATION</span>
  <span class="counter">TRACK 03</span>
</div>

### 🔌 【入力の境界（B面）】MCP / Graphify
- 巨大データを丸投げせず、必要な文脈・依存関係だけをオンデマンド取得

### 👥 【組織・体制（A面）】エージェント分業体制
- **Architect** （仕様作成） ➔ **Developer** （実装） ➔ **Reviewer** （品質検証）
- 仕様書駆動 ＋ スキル（規約注入）でコンテキストを維持・分業

### 📄 【出力の境界（B面）】中間データ ＋ スクリプト
- 構造化テキスト（JSON / Markdown等）を出力させ、決定論的スクリプトで変換

### 🛠 【実行の境界（B面）】AI統合IDE / CLI
- AIに手足を与え、「編集 ➔ ビルド ➔ テスト ➔ 自己修復」ループを回す

---

# 📝 まとめ：エンタープライズでのAI活用

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <span class="badge badge-dark">SUMMARY</span>
  <span class="counter">INDEX END</span>
</div>

1. **🔴【A面：組織論】1人に頼らず「チーム分業」させる**
   - エージェント分割・スキル注入・仕様書駆動で、コンテキスト限界を突破する。
   - いきなり作らせない。開発方式を最初に定める。

2. **🟢【B面：境界論】AIを「推論エンジン」として組み込む**
   - **出力** ：直接バイナリを作らせず中間データ（JSON等）を介する。
   - **入力** ：MCPやグラフ化でAIが読みやすい形に整えて渡す。
   - **実行** ：IDE/CLIで手足を与え、自己修正ループを回させる。

---

# 🏁 最後に：エンジニアリングの原点へ

<div style="margin-top: 20px;"></div>

### AI開発で最も重要なのは、
### 最新モデルのスペック比較ではなく、
### **「システムエンジニアリングとしての基本設計」** です。

<div style="margin: 25px 0;"></div>

<div class="point-box">
<b style="font-size: 22px;">A面（組織・分業体制） × B面（境界・インターフェース設計）</b><br>
この2つが揃って初めて、実証実験（PoC）の壁を越え、エンタープライズ品質のAI開発が実現します。
</div>

<div class="ok-box">
もう一つ言うなら、とにかく使ってみること、何ができるかを知ること。<br>
次に、どこに使えるか、を考えること（<b>イマココ！！</b> ）
</div>

---

<!-- _class: outro -->
<!-- _paginate: false -->

<div style="width: 850px; background: #23272e; border: 3px solid #c59b27; border-radius: 16px; padding: 40px 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.7); text-align: center;">
  
  <div style="display: flex; justify-content: center; gap: 15px; margin-bottom: 20px;">
    <span class="badge badge-dark" style="color: #ff5252; font-size: 16px;">■ STOP</span>
    <span class="badge badge-dark" style="color: #ffd740; font-size: 16px;">⏹ EJECT</span>
    <span class="badge badge-dark" style="color: #40c4ff; font-size: 16px;">⏪ REWIND</span>
  </div>

  <h1 style="font-size: 42px; color: #ffffff; margin: 10px 0; justify-content: center; border: none;">
    ご清聴ありがとうございました
  </h1>

  <div style="font-family: 'Share Tech Mono', monospace; font-size: 18px; color: #c59b27; margin: 15px 0; letter-spacing: 2px;">
    --- END OF TAPE [ SIDE A & SIDE B ] ---
  </div>

  <div style="font-size: 16px; color: #aaa; margin-top: 20px;">
    H協システム開発部会 2026 / 質疑応答 ＆ ディスカッション
  </div>

</div>
