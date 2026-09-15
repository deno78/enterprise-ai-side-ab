---
marp: true
html: true
theme: default
size: 16:9
paginate: true
header: "若手スキルアップ研修会 ｜ その仕事、下から見るか、上から見るか"
footer: "具体化と抽象化に見る観点の転換 ｜ 「Whyで考える」"
style: |
  @import url('https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@500;700;900&family=JetBrains+Mono:wght@700&display=swap');

  :root {
    --bg-main: #f8fafc;
    --text-main: #0f172a;
    --text-muted: #475569;
    --brand-primary: #2563eb;
    --brand-dark: #1e3a8a;
    --accent-ch1: #0284c7;
    --accent-ch1-light: #e0f2fe;
    --accent-ch2: #ea580c;
    --accent-ch2-light: #ffedd5;
    --accent-ch3: #16a34a;
    --accent-ch3-light: #dcfce7;
    --card-bg: #ffffff;
    --border-color: #cbd5e1;
  }

  section {
    font-family: 'Zen Kaku Gothic New', 'Meiryo', sans-serif;
    font-size: 23px;
    padding: 32px 45px 26px 45px;
    background-color: var(--bg-main);
    color: var(--text-main);
    position: relative;
    box-sizing: border-box;
    line-height: 1.5;
  }

  header {
    font-size: 14px;
    color: #475569;
    font-weight: 800;
    letter-spacing: 0.5px;
    top: 14px;
    left: 45px;
    right: 45px;
    border-bottom: 2px solid #cbd5e1;
    padding-bottom: 4px;
  }
  footer {
    font-size: 13px;
    color: #64748b;
    font-weight: 700;
    bottom: 10px;
    left: 45px;
    right: 45px;
    border-top: 1px solid #e2e8f0;
    padding-top: 4px;
  }

  h1 {
    font-size: 33px;
    font-weight: 900;
    color: #0f172a;
    margin-top: 0;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 10px;
    letter-spacing: -0.5px;
  }
  h2 {
    font-size: 25px;
    font-weight: 800;
    color: #1e293b;
    margin-top: 0;
    margin-bottom: 8px;
  }
  h3 {
    font-size: 21px;
    font-weight: 800;
    margin: 4px 0 4px 0;
  }

  .badge {
    display: inline-block;
    font-size: 14px;
    font-weight: 900;
    padding: 3px 12px;
    border-radius: 9999px;
    letter-spacing: 0.5px;
    vertical-align: middle;
  }
  .badge-blue { background-color: #dbeafe; color: #1d4ed8; }
  .badge-ch1 { background-color: var(--accent-ch1-light); color: var(--accent-ch1); }
  .badge-ch2 { background-color: var(--accent-ch2-light); color: var(--accent-ch2); }
  .badge-ch3 { background-color: var(--accent-ch3-light); color: var(--accent-ch3); }
  .badge-work { background-color: #fef08a; color: #854d0e; font-weight: 900; border: 1.5px solid #eab308; }

  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 6px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 6px;
  }

  /* 4コマ漫画用画像＆吹き出し重ね合わせコンテナ */
  .manga-box {
    position: relative;
    width: 525px;
    height: 525px;
    margin: 0 auto;
  }
  .manga-photo {
    width: 100%;
    height: 100%;
    display: block;
    border-radius: 8px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.22);
  }
  .fukidashi {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-family: 'Zen Kaku Gothic New', sans-serif;
    font-weight: 900;
    color: #0f172a;
    line-height: 1.25;
    box-sizing: border-box;
    pointer-events: none;
    user-select: none;
  }
  .fukidashi-v {
    writing-mode: vertical-rl;
    text-orientation: upright;
    letter-spacing: 0.5px;
  }

  .card {
    background-color: var(--card-bg);
    border: 1.5px solid var(--border-color);
    border-radius: 12px;
    padding: 14px 18px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.06);
    font-size: 21px;
  }
  .card-ch1 { border-top: 6px solid var(--accent-ch1); }
  .card-ch2 { border-top: 6px solid var(--accent-ch2); }
  .card-ch3 { border-top: 6px solid var(--accent-ch3); }
  .card-blue { border-top: 6px solid var(--brand-primary); }

  .callout {
    background-color: #eff6ff;
    border-left: 6px solid var(--brand-primary);
    border-radius: 0 8px 8px 0;
    padding: 10px 16px;
    margin: 8px 0;
    font-size: 20px;
    font-weight: 700;
  }
  .callout-ch1 { background-color: var(--accent-ch1-light); border-left: 6px solid var(--accent-ch1); }
  .callout-ch2 { background-color: var(--accent-ch2-light); border-left: 6px solid var(--accent-ch2); }
  .callout-ch3 { background-color: var(--accent-ch3-light); border-left: 6px solid var(--accent-ch3); }

  .work-box {
    background: linear-gradient(135deg, #ffffff 0%, #fefce8 100%);
    border: 2px dashed #eab308;
    border-radius: 12px;
    padding: 12px 18px;
    margin-top: 4px;
  }
  .choice-card {
    background: #ffffff;
    border: 2px solid #cbd5e1;
    border-radius: 10px;
    padding: 12px 16px;
    font-size: 19.5px;
  }
  .choice-card.highlight {
    border-color: #eab308;
    background-color: #fffef0;
    box-shadow: 0 0 0 1px #eab308;
  }

  .title-bg {
    background: radial-gradient(circle at 10% 20%, #1e3a8a 0%, #0f172a 90%);
    color: #ffffff;
  }
  .title-bg header, .title-bg footer { border: none; color: #94a3b8; }

  .chapter-bg-1 { background: linear-gradient(135deg, #075985 0%, #0f172a 100%); color: #ffffff; }
  .chapter-bg-2 { background: linear-gradient(135deg, #9a3412 0%, #0f172a 100%); color: #ffffff; }
  .chapter-bg-3 { background: linear-gradient(135deg, #166534 0%, #0f172a 100%); color: #ffffff; }
  .chapter-slide header, .chapter-slide footer { border: none; color: #94a3b8; }

  ul { margin: 4px 0; padding-left: 24px; }
  li { margin-bottom: 4px; }
  strong { color: #0f172a; font-weight: 800; }
  .text-muted { color: var(--text-muted); font-size: 0.88em; }
  .why-highlight {
    background: linear-gradient(transparent 60%, #fef08a 60%);
    font-weight: 900;
    color: #b45309;
    padding: 0 4px;
  }
---

<!-- _class: title-bg -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "若手スキルアップ研修会 ｜ 40分セッション" -->

# <span style="font-size: 44px; line-height: 1.25; color: #f8fafc; font-weight: 900;">その仕事、<br><span style="color: #60a5fa;">下から見るか、上から見るか</span></span>

### <span style="color: #cbd5e1; font-weight: 700; font-size: 24px;">― 具体化と抽象化に見る観点の転換 ｜ <span style="color: #fde047;">「Whyで考える」</span> ―</span>

<div style="margin-top: 36px; display: flex; align-items: center; gap: 16px;">
  <span class="badge badge-blue" style="font-size: 16px; padding: 6px 16px;">40分講演</span>
  <span style="font-size: 18px; color: #cbd5e1; font-weight: 700;">対象：若手社員・システム開発に携わるすべての方</span>
</div>

<!--
【スピーカーノート（想定時間：1分）】
皆さんこんにちは！若手スキルアップ研修会へようこそ。
本日のテーマは『その仕事、下から見るか、上から見るか 〜具体化と抽象化に見る観点の転換〜』です。
本日の最重要キーワードはズバリ【Whyで考える】です。
仕事をしていると、「言われた通りに真面目にやったのに怒られた」「良かれと思って要望を聞いたら製品がぐちゃぐちゃになった」という理不尽な悲劇によく遭遇します。
なぜそんなことが起きるのか？ 答えは「How（やり方）」ばかり見て、「Why（なぜやるのか）」を見失っているからです。
大講堂の後ろの席の皆さんも、ぜひリラックスして思考実験を楽しんでください！
-->

---

# 😫 真面目にやっているのに、なぜか悲劇が起きる…

<div class="grid-2">
  <div class="card" style="border-left: 6px solid #ef4444;">
    <h3 style="color: #b91c1c;">🌀 現場の「3大あるある悲劇」</h3>
    <ul>
      <li><strong>「仕様書通りに作ったのに動かない」</strong><br>誰も悪くないはずなのに、テストで大炎上</li>
      <li><strong>「お客様の要望を全部入れたのに不評」</strong><br>親切に機能を追加したのに「使いにくい」と酷評</li>
      <li><strong>「絵に描いた餅だと笑っていたら…」</strong><br>誰も完成形が分からずプロジェクトが漂流</li>
    </ul>
  </div>

  <div class="card" style="border-left: 6px solid #f59e0b; background-color: #fffbeb;">
    <h3 style="color: #b45309;">💡 原因：手元の「How」に囚われている</h3>
    <div style="font-size: 21px; margin-top: 6px;">
      私たちは普段、手元の<strong>「具体・How（どう作るか）」</strong>に目を奪われがちです。
    </div>
    <div class="callout" style="margin-top: 12px; font-size: 19px; background-color: #ffffff; border-color: #f59e0b;">
      👉 <strong>本日の鍵：</strong>一歩引いて<span class="why-highlight">「Why（そもそも何のため？）」</span>から問い直す力を手に入れよう！
    </div>
  </div>
</div>

<!--
【スピーカーノート（想定時間：1.5分）】
一生懸命頑張っているのに、なぜか結果が裏目に出てしまう。
自分の担当範囲を完璧にこなしたのにシステムが動かない。ユーザーの要望を聞いてボタンを追加したのに怒られる。
これらはすべて、皆さんのスキル不足ではなく、「手元のHow（やり方）」に視野が固定されてしまっていることが原因です。
川下に立ちながら、同時に川上の「Why（そもそも何のために？）」を見晴らす。この視座の転換を学んでいきます。
-->

---

# 🎯 本日のアジェンダ：3つの現場ストーリー

<div class="callout" style="font-size: 21px; font-weight: 800; margin-bottom: 12px;">
  ゴール：手元の「How（作業）」から「Why（本質）」へ視点を引き上げ、観点を反転させる！
</div>

<div class="grid-3">
  <div class="card card-ch1">
    <span class="badge badge-ch1">第1章</span>
    <h3 style="color: var(--accent-ch1);">職域の線引き</h3>
    <p class="text-muted">【組織と境界】<br>すき間に落ちたタスクと<br>見捨てられる川下<br><strong>＋ 4コマ ＆ 思考実験①</strong></p>
  </div>

  <div class="card card-ch2">
    <span class="badge badge-ch2">第2章</span>
    <h3 style="color: var(--accent-ch2);">ユーザー意見の改善</h3>
    <p class="text-muted">【製品とビジョン】<br>声を聞きすぎて迷走する<br><span class="why-highlight">Whyなきキメラ端末</span><br><strong>＋ 4コマ ＆ 思考実験②</strong></p>
  </div>

  <div class="card card-ch3">
    <span class="badge badge-ch3">第3章</span>
    <h3 style="color: var(--accent-ch3);">絵に描いた餅</h3>
    <p class="text-muted">【未来とイメージ】<br>誰も正解を知らない時<br>餅を描く本当の価値<br><strong>＋ 4コマ ＆ 思考実験③</strong></p>
  </div>
</div>

<!--
【スピーカーノート（想定時間：1.5分）】
本日のアジェンダです。今回はシステム開発のリアルな3つのテーマを深掘りします。
第1章は「職域の線引き」。きっちり分担したはずの組織で、なぜ狭間にボールが落ちて川下が炎上するのか。
第2章は「ユーザー意見の改善」。お客様ファーストで要望を足し算した結果、なぜWhyを見失ったキメラ端末が生まれるのか。
第3章は「絵に描いた餅」。机上の空論とバカにされがちな餅が、実は未知のプロジェクトを救う羅針盤になる理由。
各章に4コマ漫画と思考実験を用意しています。
-->

---

# 🙋‍♂️ Speaker & 本日のスタンス

<div class="grid-2">
  <div class="card card-blue">
    <h3>👨‍💼 スピーカー紹介</h3>
    <div style="display: flex; gap: 14px; align-items: center; margin-top: 6px;">
      <div style="width: 60px; height: 60px; border-radius: 50%; background-color: #dbeafe; display: flex; align-items: center; justify-content: center; font-size: 28px;">
        💻
      </div>
      <div>
        <div style="font-size: 22px; font-weight: 900;">システム開発部 メンター担当</div>
        <div style="font-size: 16px; color: var(--text-muted);">開発・要件定義・アーキテクチャ設計</div>
      </div>
    </div>
    <ul style="font-size: 19px; margin-top: 10px;">
      <li>仕様書の行間を巡って数々の炎上を経験してきた元・若手SE</li>
      <li>「HowではなくWhyを問う」ことで仕事が激変した体験を共有！</li>
    </ul>
  </div>

  <div class="card" style="background-color: #f8fafc; border: 2px dashed #94a3b8;">
    <h3>🤝 本日のグラウンドルール</h3>
    <ol style="font-size: 19px; margin-top: 6px; line-height: 1.6;">
      <li><strong>「正解当てテスト」ではない！</strong><br><span class="text-muted">現場のモヤモヤを言語化して楽しむ場です。</span></li>
      <li><strong>「あるある！」と笑い飛ばす</strong><br><span class="text-muted">4コマを見ながら「うちの現場だ…」と共感してください。</span></li>
      <li><strong>自分の普段の仕事に引き寄せる</strong><br><span class="text-muted">「自分ならどう動くか」を直感で考えましょう。</span></li>
    </ol>
  </div>
</div>

<!--
【スピーカーノート（想定時間：1.5分）】
私自身、若い頃は「仕様書に書いてないから私の仕事じゃありません！」と主張して先輩と衝突したり、言われた要望を全部実装して画面をボタンだらけにして怒られたり、痛い失敗を山ほどしてきました。
今日の研修は、皆さんに説教をする場ではありません。「わかる、そういうことあるよね」と笑い合いながら、明日からの現場をちょっと楽にする知恵を持ち帰る場にしてください。
-->

---

# 🌊 「川上（抽象・Why）」と「川下（具体・How）」

<div class="grid-2">
  <div class="card" style="border-left: 6px solid #0284c7;">
    <span class="badge badge-blue">川下 ＝ 具体（Concrete）</span>
    <h3 style="color: #0284c7; margin-top: 4px;">下から見る ｜ 虫の目（How）</h3>
    <ul>
      <li><strong>問い：</strong>「How（どう作るか？ 手順は？）」</li>
      <li><strong>対象：</strong>ソースコード、目前のタスク、画面設計</li>
      <li><strong>価値：</strong>実際に動かす力、緻密さ、実装スピード</li>
      <li><span style="color: #b91c1c; font-weight: 700;">⚠️ 罠：</span>部分最適。森の崩壊に気づかない</li>
    </ul>
  </div>

  <div class="card" style="border-left: 6px solid #7c3aed;">
    <span class="badge badge-purple">川上 ＝ 抽象（Abstract）</span>
    <h3 style="color: #7c3aed; margin-top: 4px;">上から見る ｜ 鳥の目（Why）</h3>
    <ul>
      <li><strong>問い：</strong><span class="why-highlight">「Why（そもそも何のため？ 誰のため？）」</span></li>
      <li><strong>対象：</strong>全体目的、ビジネス価値、製品ビジョン</li>
      <li><strong>価値：</strong>本質を見抜く力、方向性の決定、軌道修正</li>
      <li><span style="color: #b91c1c; font-weight: 700;">⚠️ 罠：</span>実装を知らないと机上の空論になる</li>
    </ul>
  </div>
</div>

<div class="callout" style="text-align: center; font-size: 21px; font-weight: 800; margin-top: 10px;">
  🔑 重要なのは、<strong>川下（How）で手を動かしながら、川上（Why）を見晴らす「往復運動」</strong>！
</div>

<!--
【スピーカーノート（想定時間：2分）】
川下（具体）は「How（どう作るか）」の世界です。これがないとモノは動きません。
しかし川下だけに閉じこもると、「自分の担当モジュールは動いたから、システム全体が止まっても関係ない」という部分最適に陥ります。
一方の川上（抽象）は、「Why（そもそも何のために？）」という全体目的の世界です。
この2つの視点を自由に行き来できるようになることが、プロフェッショナルの条件です。
-->

---

<!-- _class: chapter-bg-1 chapter-slide -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "若手スキルアップ研修会 ｜ 第1章" -->

<div style="margin-top: 60px;">
  <span class="badge badge-ch1" style="font-size: 20px; padding: 6px 18px;">第 1 章</span>
  <h1 style="font-size: 46px; margin-top: 20px; color: #ffffff; font-weight: 900;">
    きっちり線引きされた職域
  </h1>
  <p style="font-size: 25px; color: #bae6fd; margin-top: 10px; font-weight: 700;">
    〜 中間に落ちたタスクと、見捨てられる川下の負担 〜
  </p>
</div>

<!--
【スピーカーノート（想定時間：0.5分）】
それでは第1章に入ります。
『きっちり線引きされた職域 〜中間に落ちたタスクと、見捨てられる川下の負担〜』。
まずは現場で本当によくある光景を4コマ漫画で見てみましょう。
-->

---

# 🎭 【4コマ】きっちり線引きされた職域の悲劇

<div class="manga-box">
  <img src="1章4コマ.jpg" class="manga-photo" alt="第1章 4コマ漫画">
  <!-- コマ1 左上吹き出し -->
  <div class="fukidashi fukidashi-v" style="top: 8.5%; left: 3.5%; width: 7.5%; height: 16%; font-size: 12px;">
    私の職域は<br>ここまでです！
  </div>
  <!-- コマ3 左吹き出し上書き補正 -->
  <div class="fukidashi fukidashi-v" style="top: 57.5%; left: 3.2%; width: 8%; height: 17%; font-size: 11.5px; background: #ffffff; border-radius: 50%;">
    エラーハンドリングが<br>定義されてない!?
  </div>
</div>

<!--
【スピーカーノート（想定時間：2分）】
この4コマ、身に覚えがありませんか？
設計者は「仕様書通りに書いた」、プログラマーは「仕様書通りにコードを書いた」。誰もサボっていません。全員が自分の「線引きされた職域」の中では100点満点です。
しかし結合テストになるとエラーで動かない。なぜなら「システム同士の狭間にある共通仕様」がどちらの担当範囲にも定義されていなかったからです。
そして最悪なのは4コマ目。「私の担当範囲外ですから」と川上が去り、川下のテスターや運用チームだけが深夜残業で火消しをさせられる。
これが「きっちり線引きされた職域」が引き起こす組織の機能不全です。
-->

---

# 🧱 組織の枠組み全体から見る：境界線の「すき間」

<div class="grid-2">
  <div class="card" style="border-left: 6px solid #ef4444;">
    <h3 style="color: #b91c1c;">⬇️ 下から見る視点（部分最適）</h3>
    <ul>
      <li>「自分の職域を守ることが誠実さ」</li>
      <li>「仕様書に書いていないことはやらない」</li>
      <li><strong>結果：境界線上に落ちたボールを誰も拾わない</strong></li>
      <li>川上は手離れの良さだけを求め、川下の苦労を想像しない</li>
    </ul>
  </div>

  <div class="card" style="border-left: 6px solid var(--accent-ch1); background-color: #f0f9ff;">
    <h3 style="color: var(--accent-ch1);">⬆️ 上から見る視点（全体最適）</h3>
    <ul>
      <li>「システム全体が無事動いて初めて全員の勝利」</li>
      <li><strong>現実の仕事は、きれいな線引きの『すき間』にこそ本質がある</strong></li>
      <li>川上は「川下がどう受け取るか？」まで考えてパスを出す</li>
      <li><span class="why-highlight">「Why（全体の目的）」</span>のために境界を越える人が組織を救う</li>
    </ul>
  </div>
</div>

<div class="callout callout-ch1" style="margin-top: 10px; font-size: 20px;">
  💡 <strong>観点の転換：</strong>「自分の持ち場を守る（How）」から、「システム全体の成功（Why）」へ視座を引き上げよう！
</div>

<!--
【スピーカーノート（想定時間：2分）】
下から見ると、「自分の職域を守る」のは真面目で正しい行動に見えます。
しかし、上から組織全体を見渡すとどうでしょうか。どんなに綺麗に職域を線引きしても、現実の開発には必ず「境界線のすき間」が発生します。
サッカーで言えば、ディフェンスとミッドフィルダーの間に転がったボールを「あそこは私のエリアじゃないから」とお互いに見送って失点しているようなものです。
一流のビジネスパーソンは、川上に立ちながら「この仕様の書き方だと後工程が困るな」と川下の負担を想像し、境界を少し踏み出してパスを出します。
-->

---

# 🧠 【Work 1】思考実験：仕様書の考慮漏れを発見！

<div class="work-box">
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <span class="badge badge-work">THINKING WORK 01</span>
    <span style="font-weight: 800; color: #854d0e; font-size: 16px;">⏱ 目安時間：3分（個人思考 1分 ＋ 周囲とシェア 2分）</span>
  </div>
  <div style="font-size: 21px; font-weight: 800; margin-top: 6px; color: #0f172a;">
    📌 状況：前工程の仕様書に「アクセス集中時のタイムアウト処理」が全く考慮されていないことに気づいた！
  </div>
</div>

<div class="grid-2" style="margin-top: 8px;">
  <div class="choice-card">
    <div style="font-weight: 900; font-size: 19px; color: #64748b;">パターン A ｜ 職域厳守型（Howの論理）</div>
    <p style="font-size: 18px; margin-top: 6px; line-height: 1.45;">
      「仕様書に書いてないし、余計なことをして怒られたくない。指示通り作って、テストでエラーが出たら指摘しよう」
    </p>
  </div>
  <div class="choice-card highlight">
    <div style="font-weight: 900; font-size: 19px; color: var(--accent-ch1);">パターン B ｜ 全体視野型（Whyの論理）</div>
    <p style="font-size: 18px; margin-top: 6px; line-height: 1.45;">
      「本番で落ちたら大惨事になるな。今のうちに『タイムアウト時の挙動はどうしますか？』と設計担当にチャットで1本声をかけよう」
    </p>
  </div>
</div>

<div style="margin-top: 8px; font-size: 19px; background: #ffffff; padding: 8px 14px; border-radius: 8px; border: 1px solid #cbd5e1; font-weight: 700;">
  💬 <strong>問いかけ：</strong>あなたの現場はどちらの空気が強いですか？ あなた自身はどちらになりがちですか？
</div>

<!--
【スピーカーノート（想定時間：3分）】
最初の思考実験です。
仕様書の抜け漏れに気づいたとき、あなたならどうしますか？
パターンAは職域を守る人です。「言われてないからやらない」。でも後で手戻りになって結局自分が深夜まで直す羽目になります。
パターンBは川上と川下の繋がりが見えている人です。いま声をつなぐだけで、未来の巨大な炎上を未然に防ぐことができます。
周囲の方と1〜2分、職場のリアルな空気感を話し合ってみてください。
-->

---

<!-- _class: chapter-bg-2 chapter-slide -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "若手スキルアップ研修会 ｜ 第2章" -->

<div style="margin-top: 60px;">
  <span class="badge badge-ch2" style="font-size: 20px; padding: 6px 18px;">第 2 章</span>
  <h1 style="font-size: 46px; margin-top: 20px; color: #ffffff; font-weight: 900;">
    ユーザー意見を取り入れた製品改善
  </h1>
  <p style="font-size: 25px; color: #fed7aa; margin-top: 10px; font-weight: 700;">
    〜 「How（要望）」を鵜呑みにせず、<span style="color: #fde047;">「Why」</span>で考える 〜
  </p>
</div>

<!--
【スピーカーノート（想定時間：0.5分）】
続いて第2章です。
『ユーザー意見を取り入れた製品改善 〜「How（要望）」を鵜呑みにせず、「Why」で考える〜』。
ユーザーの声を聴くのは絶対に正しいはずです。
しかし、なぜそれが「キメラ端末」という悲劇を招くのでしょうか？ 4コマで見てみましょう。
-->

---

# 🎭 【4コマ】全部入りキメラ端末の誕生

<div class="manga-box">
  <img src="2章4コマ.jpg" class="manga-photo" alt="第2章 4コマ漫画">
  <!-- コマ1 吹き出し中 -->
  <div class="fukidashi" style="top: 7%; left: 22.5%; width: 12%; height: 7.5%; font-size: 11px;">
    お客様アンケート<br>回収したよ！
  </div>
  <!-- コマ1 吹き出し右 -->
  <div class="fukidashi fukidashi-v" style="top: 7.5%; left: 41.5%; width: 7.5%; height: 13%; font-size: 11.5px;">
    製品改善の<br>ために！
  </div>
  <!-- コマ1 吹き出し左 -->
  <div class="fukidashi fukidashi-v" style="top: 7.5%; left: 3.2%; width: 7.5%; height: 12.5%; font-size: 11px;">
    ご意見を<br>徹底収集！
  </div>
  <!-- コマ2 吹き出し -->
  <div class="fukidashi" style="top: 7.8%; left: 54%; width: 13%; height: 13.5%; font-size: 12px;">
    「文字大きめ」<br>「物理ボタン」<br>ふむ、採用だな！
  </div>
  <!-- コマ3 左吹き出し -->
  <div class="fukidashi fukidashi-v" style="top: 57%; left: 2.8%; width: 8%; height: 15.5%; font-size: 11px; background: #ffffff; border-radius: 50%;">
    物理キーと<br>光学ズームも！
  </div>
  <!-- コマ3 右吹き出し -->
  <div class="fukidashi fukidashi-v" style="top: 57%; left: 41.5%; width: 7.5%; height: 15.5%; font-size: 11px; background: #ffffff; border-radius: 50%;">
    Hi-Fiスピーカ<br>全部乗せだ！
  </div>
  <!-- コマ4 吹き出し1 (左) -->
  <div class="fukidashi fukidashi-v" style="top: 58.5%; left: 54%; width: 7.5%; height: 12.5%; font-size: 12.5px;">
    できま<br>した！
  </div>
  <!-- コマ4 吹き出し2 (中左) -->
  <div class="fukidashi fukidashi-v" style="top: 57.5%; left: 65.5%; width: 7%; height: 11.5%; font-size: 11px;">
    なんだこの<br>キメラ…
  </div>
  <!-- コマ4 吹き出し3 (中・小) -->
  <div class="fukidashi" style="top: 65%; left: 75%; width: 3.5%; height: 5%; font-size: 15px;">
    …
  </div>
  <!-- コマ4 吹き出し4 (中右) -->
  <div class="fukidashi" style="top: 61.5%; left: 81%; width: 5.5%; height: 7.5%; font-size: 10.5px;">
    重さ<br>5kg!?
  </div>
  <!-- コマ4 吹き出し5 (右) -->
  <div class="fukidashi fukidashi-v" style="top: 58%; left: 90%; width: 7.5%; height: 12%; font-size: 11px;">
    誰が使うの<br>これ…
  </div>
</div>

<!--
【スピーカーノート（想定時間：2分）】
新型タブレットを改善しようとアンケートをとりました。
「画面の文字を大きくして」「押しやすい物理ボタンをつけて」「キーボードもほしい」「カメラも一眼レフ並みに」「いいスピーカーも」。
若手企画者は要望をすべて仕様書に盛り込みました。
そして出来上がったのは、重さ5kg、厚さ5cm、ボタンが何十個もついた「キメラ端末」です。
シニアは重くて持てず、ビジネスマンは持ち歩けず、誰も買わない最悪の製品になりました。
なぜこうなったのか？ 顧客が言った「How（手段）」をそのまま足し算し、「Why（なぜそれを求めているのか）」を考えなかったからです。
-->

---

# 🔎 具体（How）の足し算をやめ、<span class="why-highlight">「Why」</span>で考える

<div class="grid-2">
  <div class="card" style="border-left: 6px solid #ef4444;">
    <h3 style="color: #b91c1c;">❌ 失敗：顧客の「How」を鵜呑みにする</h3>
    <ul>
      <li>「このボタンをつけて」「この機能が欲しい」</li>
      <li>要望をパッチワークのように全部足し算する</li>
      <li><strong>結果：誰のためか分からない総花的なゴミになる</strong></li>
      <li>リモコンのボタンが100個あって誰も使えない状態</li>
    </ul>
  </div>

  <div class="card" style="border-left: 6px solid var(--accent-ch2); background-color: #fff7ed;">
    <h3 style="color: var(--accent-ch2);">⭕ 成功：1段抽象化して「Why」を問う</h3>
    <ul>
      <li><span class="why-highlight">「そもそも、なぜその機能が欲しいのか？」</span></li>
      <li>ヘンリー・フォードの名言：<br>
        <span style="font-size: 17px; color: #9a3412; font-style: italic;">「もし顧客に何が欲しいか聞いていたら、『もっと速い馬』と答えただろう」</span></li>
      <li>顧客が語るのは「手段（How）」。開発者が考えるべきは「真の目的（Why）」！</li>
    </ul>
  </div>
</div>

<div class="callout callout-ch2" style="margin-top: 10px; font-size: 20px;">
  💡 <strong>第2章の鍵：</strong>言われた通りのボタンを付けるな。<span class="why-highlight">「Whyで考える」</span>ことで、本質的な価値を引き算で作ろう！
</div>

<!--
【スピーカーノート（想定時間：2分）】
自動車を発明したヘンリー・フォードはこう言いました。「顧客に何が欲しいか聞いたら、『もっと速い馬が欲しい』と答えただろう」。
顧客は「How（目の前の手段）」しか語れません。しかしフォードは「Why（なぜ？）」を考えました。「顧客が本当に求めているのは馬ではない。『もっと速く移動すること』だ」。だから自動車を作ったのです。
顧客の言う「このボタンを増やして」をそのまま鵜呑みにするのはプロの仕事ではありません。
「なぜそのボタンが必要なのか？」とWhyを自問し、真の課題を見抜いて引き算をするのが製品企画・開発の真髄です。
-->

---

# 🧠 【Work 2】思考実験：「検索条件をあと15個増やして！」

<div class="work-box">
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <span class="badge badge-work">THINKING WORK 02</span>
    <span style="font-weight: 800; color: #854d0e; font-size: 16px;">⏱ 目安時間：3分（個人思考 1分 ＋ 周囲とシェア 2分）</span>
  </div>
  <div style="font-size: 21px; font-weight: 800; margin-top: 6px; color: #0f172a;">
    📌 状況：ユーザー部門から「検索画面に、あと15個の絞り込み条件ドロップダウンを追加してほしい！」と強い要望が届いた。
  </div>
</div>

<div class="grid-2" style="margin-top: 8px;">
  <div class="choice-card">
    <div style="font-weight: 900; font-size: 19px; color: #64748b;">パターン A ｜ Howを鵜呑み（キメラ化）</div>
    <p style="font-size: 18px; margin-top: 6px; line-height: 1.45;">
      「顧客要望だから断れない！」と15個の入力欄をズラリ追加。画面が真っ青になり、一般ユーザーは使い方が分からなくなる。
    </p>
  </div>
  <div class="choice-card highlight">
    <div style="font-weight: 900; font-size: 19px; color: var(--accent-ch2);">パターン B ｜ Whyで考える（本質解決）</div>
    <p style="font-size: 18px; margin-top: 6px; line-height: 1.45;">
      <span class="why-highlight">「なぜ15個も？」</span>と目的を聞く。「月末の未承認伝票を探したいだけ」と判明し、『ワンクリック未承認ボタン』を1つ提案！
    </p>
  </div>
</div>

<div style="margin-top: 8px; font-size: 19px; background: #ffffff; padding: 8px 14px; border-radius: 8px; border: 1px solid #cbd5e1; font-weight: 700;">
  💬 <strong>問いかけ：</strong>あなたが最近関わった機能で、「言われるがまま作ってキメラ化した機能」はありませんか？
</div>

<!--
【スピーカーノート（想定時間：3分）】
第2の思考実験です。
現場から「絞り込み条件を15個増やしてくれ」と言われました。
パターンAはそのまま追加。画面はごちゃごちゃになり、サーバーの検索負荷も激増します。
パターンBは「Why（なぜそれをしたいのか？）」を聞きに行きます。すると、「実は月末に未承認の伝票を一発で見つけたいだけだった」と分かります。
であれば、15個の入力欄を作る必要なんて全くないですよね。「ワンクリック未承認ボタン」を1個置けば、ユーザーも大喜び、開発工数も10分の1です。
これが「Whyで考える」威力です。
-->

---

<!-- _class: chapter-bg-3 chapter-slide -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "若手スキルアップ研修会 ｜ 第3章" -->

<div style="margin-top: 60px;">
  <span class="badge badge-ch3" style="font-size: 20px; padding: 6px 18px;">第 3 章</span>
  <h1 style="font-size: 46px; margin-top: 20px; color: #ffffff; font-weight: 900;">
    絵に描いた餅
  </h1>
  <p style="font-size: 25px; color: #bbf7d0; margin-top: 10px; font-weight: 700;">
    〜 誰も完成形をイメージできていないプロジェクトの悲劇 〜
  </p>
</div>

<!--
【スピーカーノート（想定時間：0.5分）】
最後の第3章です。
『絵に描いた餅 〜誰も完成形をイメージできていないプロジェクトの悲劇〜』。
「そんなの絵に描いた餅だ、もっと現実を見ろ！」……よく聞く言葉ですよね。
しかし、本当に絵に描いた餅は役に立たないのでしょうか？
-->

---

# 🎭 【4コマ】折り畳みタブレットの奇跡

<div class="manga-box">
  <img src="3章4コマ.jpg" class="manga-photo" alt="第3章 4コマ漫画">
  <!-- コマ1 左吹き出し -->
  <div class="fukidashi fukidashi-v" style="top: 8%; left: 3.5%; width: 7.5%; height: 22%; font-size: 12px;">
    折り畳みで<br>スマホ兼用端末<br>作って！
  </div>
  <!-- コマ1 右吹き出し -->
  <div class="fukidashi fukidashi-v" style="top: 7.5%; left: 41.5%; width: 7.5%; height: 20%; font-size: 12px;">
    もちろん<br>物理キーも<br>付けてね！
  </div>
  <!-- コマ2 トゲトゲ吹き出し -->
  <div class="fukidashi" style="top: 8%; left: 54%; width: 42%; height: 7%; font-size: 13px; color: #b91c1c;">
    そんな絵に描いた餅、売れるわけない！ 現実見て！
  </div>
  <!-- コマ3 左吹き出し -->
  <div class="fukidashi fukidashi-v" style="top: 57.5%; left: 3%; width: 8%; height: 20%; font-size: 11.5px;">
    まぁまぁ、<br>とりあえず<br>作ってみようよ
  </div>
  <!-- コマ3 右吹き出し -->
  <div class="fukidashi fukidashi-v" style="top: 57.5%; left: 41.5%; width: 7.5%; height: 20%; font-size: 11.5px;">
    3Dプリンタで<br>モック完成！
  </div>
  <!-- コマ4 吹き出し上 -->
  <div class="fukidashi" style="top: 61%; left: 52%; width: 7.5%; height: 11.5%; font-size: 11.5px;">
    できま<br>した！
  </div>
  <!-- コマ4 吹き出し下 -->
  <div class="fukidashi" style="top: 81.5%; left: 51.5%; width: 8%; height: 16%; font-size: 11px;">
    なんか<br>よく分から<br>んけど…
  </div>
  <!-- コマ4 吹き出し右 -->
  <div class="fukidashi fukidashi-v" style="top: 57.5%; left: 90.5%; width: 7.5%; height: 22%; font-size: 12px;">
    ガジェットマニアに<br>大ヒットだー！！
  </div>
</div>

<!--
【スピーカーノート（想定時間：2分）】
上司が無茶振りをしました。「折り畳めてスマホにもなってキーボードもつく端末を作ろう！」。
部下1は「そんな絵に描いた餅、技術的に無理だし売れない。現実を見ろ」と切り捨てました。
しかし部下2は、「まあまあ、粗くてもいいからまずダンボールと3Dプリンタで形にしてみようよ」と作ってみた。
すると実物を見て「あ、ここをこうすれば使えるかも！」とアイデアが連鎖し、結果的にガジェットマニアに大ヒットして新しい市場を切り拓きました。
-->

---

# 🎨 未知の領域でこそ「絵に描いた餅」が命綱になる

<div class="grid-2">
  <div class="card" style="border-left: 6px solid #ef4444;">
    <h3 style="color: #b91c1c;">❌ 「現実ばかり見る」現場の罠</h3>
    <ul>
      <li>「実現可能性（フィージビリティ）が出るまで動かない」</li>
      <li>「前例がないから作れない」「失敗の責任は誰が？」</li>
      <li><strong>結果：誰も完成形をイメージできず、座礁する</strong></li>
      <li>足元（How）だけ見て歩くと、暗闇で迷子になる</li>
    </ul>
  </div>

  <div class="card" style="border-left: 6px solid var(--accent-ch3); background-color: #f0fdf4;">
    <h3 style="color: var(--accent-ch3);">⭕ 「絵に描いた餅」の3大パワー</h3>
    <ul>
      <li><strong>① ベクトルの一致：</strong>「あそこを目指すぞ」と視線が揃う</li>
      <li><strong>② 議論の触媒：</strong>絵があるから「ここを直そう」と始まる</li>
      <li><strong>③ 未知の突破口：</strong>知らない未来を描く勇気が人を動かす</li>
    </ul>
  </div>
</div>

<div class="callout callout-ch3" style="margin-top: 10px; font-size: 20px;">
  💡 <strong>観点の転換：</strong>「食べられない餅」と捨てるな。<span class="why-highlight">「未来を手繰り寄せる北極星（ビジョン）」</span>として餅を描こう！
</div>

<!--
【スピーカーノート（想定時間：2分）】
「絵に描いた餅」はネガティブに使われがちです。
しかし、DXや新規AI開発など「誰も正解を知らない未知のプロジェクト」において、最初から食べられる本物の餅なんてどこにもありません。
粗削りでもいい。「私たちはこの世界を作りたいんだ！」という絵に描いた餅（抽象的なビジョンやプロトタイプ）を描くからこそ、チーム全員の視線が揃い、議論が動き出します。
知らないことを恐れずに、まず絵を描いてみる。これが若手にとって最強の武器になります。
-->

---

# 🧠 【Work 3】思考実験：正解のない新規AI案件！

<div class="work-box">
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <span class="badge badge-work">THINKING WORK 03</span>
    <span style="font-weight: 800; color: #854d0e; font-size: 16px;">⏱ 目安時間：3分（個人思考 1分 ＋ 周囲とシェア 2分）</span>
  </div>
  <div style="font-size: 21px; font-weight: 800; margin-top: 6px; color: #0f172a;">
    📌 状況：社内で「生成AIを使った新サービスを作れ」と特命チームに配属されたが、誰も具体的に何をすればいいか分からず沈黙している。
  </div>
</div>

<div class="grid-2" style="margin-top: 8px;">
  <div class="choice-card">
    <div style="font-weight: 900; font-size: 19px; color: #64748b;">パターン A ｜ 確実性重視（現実主義）</div>
    <p style="font-size: 18px; margin-top: 6px; line-height: 1.45;">
      「成功事例やガイドラインが完璧に固まるまで、下手な提案はせず様子を見よう。絵に描いた餅を言って恥をかきたくない」
    </p>
  </div>
  <div class="choice-card highlight">
    <div style="font-weight: 900; font-size: 19px; color: var(--accent-ch3);">パターン B ｜ 餅先行型（ビジョン提示）</div>
    <p style="font-size: 18px; margin-top: 6px; line-height: 1.45;">
      「技術的に可能か不明ですが、こんなAI画面があったら最高じゃないですか？」と手書きスケッチを投げて議論を起こす！
    </p>
  </div>
</div>

<div style="margin-top: 8px; font-size: 19px; background: #ffffff; padding: 8px 14px; border-radius: 8px; border: 1px solid #cbd5e1; font-weight: 700;">
  💬 <strong>問いかけ：</strong>プロジェクトを本当に前進させるのは、どちらのスタンスだと思いますか？
</div>

<!--
【スピーカーノート（想定時間：3分）】
最後の思考実験です。
誰も正解がわからない新規AI案件にアサインされました。
パターンAは賢い現実主義者です。でも全員がAをやったら、会議は永遠に沈黙し、プロジェクトは1ミリも進みません。
パターンBは「絵に描いた餅を描く人」です。「技術的にできるか分からないけど、こんな画面で動いたらワクワクしません？」と叩き台を出す。
すると周りのベテランが「いやそのAPIは無理だけど、こっちのモデルならできるぞ！」と動き出すのです。
未知のプロジェクトを動かすのは、いつだって「最初に粗い絵を描いた人」です。
-->

---

# 🔄 まとめ：観点が変われば「正義」は反転する

<table style="width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 18px;">
  <thead>
    <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
      <th style="padding: 10px; text-align: left; width: 22%;">テーマ</th>
      <th style="padding: 10px; text-align: left; width: 39%;">⬇️ 下から見る視点（How・具体）</th>
      <th style="padding: 10px; text-align: left; width: 39%;">⬆️ 上から見る視点（Why・抽象）</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 10px; font-weight: 800;">第1章：職域の線引き</td>
      <td style="padding: 10px;">「担当範囲をきっちりやり切る<br>（責任の明確化）」</td>
      <td style="padding: 10px; color: #0284c7; font-weight: 800;">反転 ➔ 「すき間のボールを誰も拾わず、川下が炎上する無責任」</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 10px; font-weight: 800;">第2章：顧客の意見</td>
      <td style="padding: 10px;">「顧客の要望を全部真面目に入れる<br>（顧客第一主義）」</td>
      <td style="padding: 10px; color: #ea580c; font-weight: 800;">反転 ➔ 「Whyを見失い、誰も使えないキメラ端末を生む怠慢」</td>
    </tr>
    <tr style="border-bottom: 1px solid #e2e8f0;">
      <td style="padding: 10px; font-weight: 800;">第3章：絵に描いた餅</td>
      <td style="padding: 10px;">「実現不可能な机上の空論<br>（役に立たない無駄）」</td>
      <td style="padding: 10px; color: #16a34a; font-weight: 800;">反転 ➔ 「未知の暗闇で全員のベクトルを揃える唯一の羅針盤」</td>
    </tr>
  </tbody>
</table>

<div class="callout" style="margin-top: 10px; font-size: 21px; text-align: center; font-weight: 900;">
  🎭 下から見れば「100点満点の正義」が、上から見ると「大失敗の元凶」に反転する！
</div>

<!--
【スピーカーノート（想定時間：2分）】
研修のまとめです。3つの章で見てきた景色を振り返ってみましょう。
下から見ると「職域を守る」「顧客の要望を聞く」「現実的なものだけ作る」というのは、どれも真面目で正しい行動に見えます。
しかし、上から見ると全てが真逆に反転します。
職域遵守は「無責任な分断」になり、要望の全採用は「キメラ端末」を生み、絵に描いた餅の否定は「プロジェクトの漂流」を招く。
逆に、下から見れば「役立たず」と叩かれがちな絵に描いた餅が、上から見れば「未来を照らす唯一の北極星」になる。
この反転に気づく鍵こそが、「Whyで考える」ことなのです。
-->

---

# 🎁 本日持ち帰ってほしい、たった1つのこと

<div style="background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); border-radius: 16px; padding: 22px 28px; color: #ffffff; text-align: center; box-shadow: 0 8px 24px rgba(0,0,0,0.2);">
  <div style="font-size: 22px; color: #93c5fd; font-weight: 700;">今日、これだけは絶対に持ち帰ってください！</div>
  <div style="font-size: 42px; font-weight: 900; color: #fde047; margin: 10px 0; letter-spacing: 1px;">
    「How（やり方）」の前に、<br>まず「Why（なぜ？）」で考える！
  </div>
  <div style="font-size: 20px; color: #e2e8f0; font-weight: 500;">
    作業に追われた時こそ、1回立ち止まって<span style="color: #67e8f9; font-weight: 800;">「そもそも何のためだっけ？」</span>と自問する。
  </div>
</div>

<div class="grid-3" style="margin-top: 14px;">
  <div class="card card-ch1" style="padding: 10px 14px; font-size: 18px;">
    <strong>🧱 職域のすき間で</strong><br>「Why：システム全体を成功させるために」境界を一歩越える
  </div>
  <div class="card card-ch2" style="padding: 10px 14px; font-size: 18px;">
    <strong>🧩 要望を聞いた時</strong><br>「Why：顧客が本当に叶えたい課題は何？」と目的を深掘りする
  </div>
  <div class="card card-ch3" style="padding: 10px 14px; font-size: 18px;">
    <strong>🎨 先が見えない時</strong><br>「Why：目指す理想の未来は何か？」とまず粗い餅を描く
  </div>
</div>

<!--
【スピーカーノート（想定時間：2分）】
今日、たくさんの話をしましたが、たった1つだけ持ち帰るならこれです。
「How（どうやるか）」の前に、まず「Why（なぜやるのか）」で考える！
明日会社に行って、タスクに追われてキーボードを叩きまくっている自分に気づいたら、ふと1回手を止めてください。
「そもそも、なぜこの仕事をやっているんだっけ？」
この1秒の自問が、あなたを単なる「作業者」から「自律的なプロフェッショナル」へと変貌させます。
-->

---

<!-- _class: title-bg -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "若手スキルアップ研修会 ｜ おわりに" -->

# <span style="font-size: 40px; color: #f8fafc; font-weight: 900;">その仕事、下から見るか、上から見るか</span>

<div style="font-size: 24px; color: #cbd5e1; margin-top: 16px; line-height: 1.6;">
  川下で<strong>泥臭く手を動かし、やりきる力（How）</strong>。<br>
  川上から<strong>本質を見晴らし、未来を描く力（Why）</strong>。<br>
  どちらか一方ではなく、<br>
  <span style="color: #60a5fa; font-weight: 900;">「どちらからも見られる自由」</span>を手に入れたとき、仕事は劇的に面白くなります。
</div>

<div style="margin-top: 30px; padding: 14px 22px; background: rgba(255,255,255,0.08); border-radius: 12px; border: 1.5px solid rgba(255,255,255,0.2);">
  <div style="font-size: 22px; font-weight: 900; color: #facc15;">💬 質疑応答 ＆ 感想共有タイム</div>
  <div style="font-size: 17px; color: #e2e8f0; margin-top: 4px;">
    本日の感想、現場でのモヤモヤ、「明日からWhyで考えます！」の宣言など、何でも大歓迎です！
  </div>
</div>

<!--
【スピーカーノート（想定時間：6分（まとめ1分 ＋ 質疑応答5分））】
最後に、タイトルの問いにお答えして締めくくりたいと思います。
「その仕事、下から見るか、上から見るか」。
答えは、「両方から見る」です。
川下を知っているからこそ、地に足のついた設計ができます。
川上を知っているからこそ、手元のコードに魂が宿ります。
下からも上からも見られる自由を、ぜひ今日から手に入れてください。
ご清聴ありがとうございました！ これより質疑応答に入ります。
-->
