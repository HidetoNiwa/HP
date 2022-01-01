---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Slackのカスタム絵文字の移行"
subtitle: "Slackのカスタム絵文字のエクスポート/インポート方法"
summary: "Slackのカスタム絵文字のエクスポート/インポート方法"
authors: [HidetoNiwa]
tags: [slack]
categories: [slack]
date: 2020-09-27T02:38:54+09:00
lastmod: 2020-09-27T02:38:54+09:00
featured: false
draft: false

card_image: "card/post/slack-emoji-move.png"
# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

こんにちは、どと～ること、にゎ～んです。NHK学生ロボコンもついに2021のルールが発表されましたね。

Slackのワークスペースの移行が行われていたりしてます。

そのSlackのワークスペース移行に当たって、「カスタム絵文字」（自分たちで追加したスタンプのこと）の移行が面倒になったりします。
移行の方法に関して、インターネットの広い海に書かれていたりしますが、Slack apiの仕様が変更になったりして方法が変わっていたので2020/09現在の方法に関して、
備忘録をかねて記載していきたいと思います。

## 基本環境

Windows10(64bit)　2020/09/27現在

※MacやLinuxでもNode.jsさえインストールしてしまえば同様だと思います。（未検証）

## 絵文字をSlackからエクスポート

### Node.jsのインストール

[Node.js 公式サイト](https://nodejs.org/ja/)へアクセス、自分のPCに合うインストーラをダウンロード。（筆者は12.18.4LTSをインストール）

インストーラがダウンロード出来たら適当にYesをクリックしていきインストールする。<br>
（この時、Add PATHにチェックが入っているか確認する。）

### 各種モジュールインストール

下記コマンドをコマンドプロンプト/PowerShellで実行し、インストールを行う。

```bash
npm install slack-node
npm install request
npm install fs
```

### Slack API Tokenの準備

[Slack api](https://api.slack.com/)へアクセスし、画面中央の"Start Building"をクリックする。

すると、下記画像の様に出てくるので、適当に Slack App 名を決め、インストールするワークスペースを指定し、"create app"をクリックする。
{{< figure src="/img/post/slack/emoji-app.JPG">}}

続いて、Permissionsをクリックする。これによって、Permission管理ができる。
{{< figure src="/img/post/slack/emoji-app2.JPG" width="75%">}}

ページ中央部に"Scopes"があるので、"Add an OAuth Scope"をクリックし、"emoji:read"を追加する。(赤色下線部)<br>
そして、ページ上部の"Install App to Workspace"をクリックする。
{{< figure src="/img/post/slack/emoji-app3.JPG" width="65%">}}

そして、ワークスペース連携の許可を求められるので、**許可**する。<br>
すると、"Bot User OAuth Access Token"が表示される。このTokenは後々使用するのでCopyしてメモる。
{{< figure src="/img/post/slack/emoji-app4.JPG" width="65%">}}

### インポートスクリプト作成

インポートしたいディレクトリで、"app.js"といったファイル名で下記ファイルを作成する。<br>
また、同じディレクトリに"image"といったディレクトリも作成する。

```js app.js
var Slack = require('slack-node');
var request = require('request');
var fs = require('fs');

apiToken = "<API Token>"; // Slack APIトークンを" "内に貼り付け
slack = new Slack(apiToken);

slack.api("emoji.list", function (err, response) {
    for(key in response.emoji){
        url = response.emoji[key];
        //エイリアスは無視
        if(url.match(/alias/)){
            continue;
        }

        // 取得対象の拡張子
        extention = url.match(/\.[^\.]+$/);

        request
        .get(url)
        .on('response', function (res) {
        })
        .pipe(fs.createWriteStream('image/' + key + extention));
    }
});
```

### 実行

下記コマンドを実行して、カスタム絵文字のダウンロードを行う。

```bash
node app.js
```

## 絵文字のSlackへインポート

### Slack Custom Emoji Manager(Chrome拡張機能) のインストール

[Slack Custom Emoji Manager(Chrome拡張機能)](https://chrome.google.com/webstore/detail/slack-custom-emoji-manage/cgipifjpcbhdppbjjphmgkmmgbeaggpc/related)へchrome/edge（最新版）等、chrome拡張機能が使えるブラウザでアクセスし、「chromeに追加」をクリック

すると、https://(ワークスペース名).slack.com/customize/emoji へアクセスすると下記画像の様になる。
"ここに追加したい絵文字をドラック＆ドロップ"で投下すると、絵文字の追加が順次行われていく。
{{< figure src="/img/post/slack/slack-stamp-ext.JPG" width="65%">}}

## まとめ

以上で、Slackのカスタム絵文字の移行は完了です！

APIは生物なので、開発の具合やユーザ要望によって仕様変更が起こるのは多々ですよね...<br>
今後はどうなっていくのやら:thinking_face:

## 参考情報

chrome拡張機能を入れると、"すべての絵文字をダウンロード"とボタンがあるがダウンロードすることは出来ない。<br>
（API仕様変更のため...?，作成者様の[Qiita記事](https://qiita.com/nabekou29/items/83e11a58724517f66cad#%E3%81%A7%E3%81%8D%E3%81%9F%E3%82%82%E3%81%AE)にはできると書かれているのだが...）

下記サイトを参考にさせていただきました。

- [Slack カスタム絵文字 一括ダウンロード・インストール方法 まとめ](https://blog.ef-4.co.jp/slack-%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0%E7%B5%B5%E6%96%87%E5%AD%97-%E4%B8%80%E6%8B%AC%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89%E3%83%BB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC/)
- [Slackのカスタム絵文字を一括ダウンロード・削除するChrome拡張を作ってみた](https://qiita.com/nabekou29/items/83e11a58724517f66cad#%E3%81%A7%E3%81%8D%E3%81%9F%E3%82%82%E3%81%AE)
