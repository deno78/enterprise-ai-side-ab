# エンタープライズAI開発のA面／B面 実験リポジトリ
### 〜 実証実験止まりを脱却する「分業（組織論）」と「境界設計（システム論）」 〜

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Antigravity](https://img.shields.io/badge/AI_Engine-Antigravity%20%2F%20OpenCode-green.svg)](#)
[![Python](https://img.shields.io/badge/Backend-Python%20Flask-3776AB.svg?logo=python&logoColor=white)](#)
[![Vue.js](https://img.shields.io/badge/Frontend-Vue.js%203%20(CDN)-4FC08D.svg?logo=vuedotjs&logoColor=white)](#)

本リポジトリは、講演・勉強会資料**『エンタープライズAI開発のA面／B面』**（添付の [`エンタープライズAI開発のA面／B面.md`](./エンタープライズAI開発のA面／B面.md)）で解説された、**AIコーディングにおける「単一丸投げ」と「エージェント分業」の比較検証実験**を誰でも再現・検証できるようにパッケージングしたプロジェクトです。

---

## 📼 背景：A面とB面のアーキテクチャ思想

```
+-------------------------------------------------------------------------+
|                  エンタープライズAI開発の全体アーキテクチャ               |
|                                                                         |
|  [B面: 入力の境界]     -->   [A面: 組織・分業体制]   -->   [B面: 出力の境界]  |
|  MCP / Graphify              エージェント分業              中間データ (JSON等)   |
|  必要な文脈だけ取得           (設計->実装->品質検証)        決定論的スクリプト    |
|                                     |                                   |
|                                     v                                   |
|                             [B面: 実行の境界]                            |
|                             AI統合IDE / CLI                             |
|                             自律エラー自己修復ループ                      |
+-------------------------------------------------------------------------+
```

1. **🔴【A面：組織・体制論】1人のAIに丸投げするのをやめ、チームで開発する**
   - 長文プロンプトや会話の長期化で生じる**「コンテキスト限界（忘却・破綻）」**を、専門エージェントの分業（設計・実装・テスト・ドキュメント）とスキル（開発規約・チェックリスト）によって突破する。
2. **🟢【B面：境界設計論】AIを「推論エンジン」として正しく組み込む**
   - **出力の境界**: いきなりExcelやバイナリを作らせず、構造化テキスト（JSON/Markdown）を出力させてスクリプトで変換する。
   - **入力の境界**: 巨大データを丸投げせず、MCPや依存関係グラフで必要な文脈だけを渡す。
   - **実行の境界**: ファイル直接編集・テスト実行・エラー自己修復ができる手足（IDE/CLI）を与える。

---

## 🧪 実験内容：自治体施設予約システム開発

共通の要件定義書（[`spec.md`](./spec.md)）から、以下の2つの手法でシステムを生成・比較検証しました。

| 手法 | 方式 | プロンプト・指示方法 |
|---|---|---|
| **alpha（単一丸投げ）** | 1つのAIに全工程を一括指示 | `spec.md の中身を読み込んで、そのとおりにシステムを開発してください。` |
| **beta（組織・分業）** | 役割と規約（スキル）を定義し分業 | `AGENTS.md` + `skills/` を注入し `@architect spec.md に従って開発を開始して` |

### システム要件（[`spec.md`](./spec.md) より抜粋）
- **概要**: 市民が体育館や会議室を検索・予約し、模擬QR決済と予約票PDFを出力する自治体システム
- **技術制約**: Python Flask（バックエンド） + Vue.js 3 CDN（フロントエンド） + SQLite（単一サーバー構成）
- **多言語対応**: 日本語・英語・中国語
- **成果物**: `dist/` ディレクトリに仕様書（日英）、利用者マニュアル（日英）、ソースコード一式

---

## 📊 比較検証結果（評価レポート）

詳細な評価は [`report.md`](./report.md) に記録されています。

| 観点 | exam-alpha（単一丸投げ） | exam-beta（組織・分業） |
|---|---|---|
| **アーキテクチャ** | モノリシック（1ファイルに全集中） | **モジュール分割（Flask Blueprint設計）** |
| **Python品質** | 可読性はあるがエラー処理が粗い | **堅牢・構造化・Problem Detailsエラー応答** |
| **フロントエンド品質** | 単一HTMLに690行ベタ書き・SFCなし | **13コンポーネント分割、SPA構成、Store管理** |
| **多言語対応** | 辞書の重複・ハードコード・保守破綻 | **vue-i18n で適切に外部化・分離管理** |
| **管理・監査機能** | なし（一般画面のみ） | **施設/予約の管理画面 + 操作ログ（監査証跡）** |
| **ドキュメント** | `spec.md` のみ | **アーキテクチャ設計書4種 + エージェント仕様** |
| **総合評価** | ★★☆☆☆ (2/5) 簡易プロト止まり | **★★★★★ (5/5) 実運用レベルの拡張性・保守性** |

> 📁 実際の生成コードは [`experiments/exam-alpha`](./experiments/exam-alpha) および [`experiments/exam-beta`](./experiments/exam-beta) で直接ご確認いただけます。

---

## 🛠 再現手順（How to Reproduce）

本リポジトリをクローンして、お好みのAI開発ツールで実験を再現できます。

```bash
git clone https://github.com/deno78/enterprise-ai-side-ab.git
cd enterprise-ai-side-ab
```

### 1. `agy` (Antigravity CLI) で再現する場合

Antigravity CLI (`agy`) を使用して、自律エージェントに開発タスクを依頼します。

```bash
# 【beta手法: エージェント分業による開発の再現】
agy -p "AGENTS.md と skills/ 配下の指示書に基づき、spec.md に従って自治体施設予約システムを設計・実装してください。" --dangerously-skip-permissions
```

- `--dangerously-skip-permissions` を付与することで、ファイルの作成・編集・テスト実行をノンブロッキングで自律的に完遂します。
- 必要に応じて、`--agent` フラグや対話モード（`agy`）でのステップ実行も可能です。

### 2. `opencode` で再現する場合

本リポジトリには [`.opencode/`](./.opencode) 設定ファイルが同梱されています。

```bash
# OpenCode を起動
opencode

# プロンプト入力画面で以下を入力:
@architect spec.md に従って開発を開始して
```

`.opencode/opencode.json` 内で `architect`, `developer`, `reviewer` の各エージェントおよび `system-design`, `code-review-checklist` スキルが自動的に読み込まれ、分業開発がスタートします。

### 3. Antigravity IDE / VS Code 等で再現する場合

- IDE のチャットパネルを開き、`AGENTS.md` をコンテキストに追加した上で、各ロール（設計者 → 開発者 → QA → ドキュメント）のステップを指示してください。

---

## 🚀 生成されたアプリケーションの起動・動作確認

エージェント分業によって生成された `exam-beta` のアプリケーションは、以下の手順ですぐにローカル起動できます。

```bash
cd experiments/exam-beta

# 1. 依存ライブラリのインストール
pip install -r requirements.txt

# 2. サーバー起動（初期シードデータが自動投入されます）
python app.py

# 3. ブラウザでアクセス
# http://localhost:5000
```

### テストアカウント
- 一般市民ユーザー: `citizen / password123`
- 自治体職員（管理者）: `staff / admin123`

---

## 📂 リポジトリ構成

```
.
├── README.md                      # 本ドキュメント
├── spec.md                        # システム要件定義書（施設予約システム）
├── AGENTS.md                      # エージェント分業体制・役割分担の定義
├── report.md                      # alpha / beta ソースコード評価レポート
├── エンタープライズAI開発のA面／B面.md # 講演・勉強会用スライド資料 (Marp形式)
├── skills/                        # スキル・規約定義ディレクトリ
│   ├── design/instructions.md     # 設計者エージェント向け指示
│   ├── backend/instructions.md    # バックエンド開発者向け指示
│   ├── ui/instructions.md         # フロントエンド開発者向け指示
│   ├── qa/instructions.md         # 品質保証・テスター向け指示
│   └── documentation/instructions.md # ドキュメント作成者向け指示
├── .opencode/                     # OpenCode 用設定・エージェント・スキル定義
├── experiments/                   # 実際の実験生成成果物
│   ├── exam-alpha/                # 単一AI丸投げで生成されたコード一式
│   └── exam-beta/                 # エージェント分業で生成されたコード一式
└── .gitignore
```

---

## 📄 ライセンス
本リポジトリのコードおよび資料は [MIT License](LICENSE) のもとで公開されています。社内勉強会やAI開発の設計指針として自由にご活用ください。
