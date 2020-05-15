---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Hugoでの投稿の仕方"
subtitle: ""
summary: "Hugoプロジェクトの作成方法&静的なサイトの生成方法"
authors: [HidetoNiwa]
tags: [Hugo]
categories: [Hugo]
date: 2020-05-15T00:27:50+09:00
lastmod: 2020-05-15T00:27:50+09:00
featured: false
draft: false

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
## はじめに

こんにちは、どと～ることにゎ～んです。さて以前、HugoをWindows上で環境構築する方法を示しました。今回はHugoを使ってプロジェクトを作成する方法を示したいと思います。

## Hugoプロジェクトの作成

PowerShell、Terminalなど使用OSにおけるコマンドコンソール（以下、コマンドライン）を開き、プロジェクトを作成したいディレクトリにcdやmkdirを使用して移動します。移動した先で、
{{< highlight Shell "linenos=false">}}
hugo new site test
{{< /highlight >}}
と実行します。すると、そのディレクトリに、**test**といったフォルダが作成されます。その中身をtreeコマンドを用いて確認すると、
{{< highlight Shell "linenos=false">}}
test
├─archetypes
├─content
├─data
├─layouts
├─resources
│  └─_gen
│      ├─assets
│      └─images
├─static
└─themes
{{< /highlight >}}
といった階層になっているのが確認できます。

## テーマ導入

これでプロジェクトは完成しましたが、これではサイトとして表示されないので、テーマを導入していきたいと思います。ここでは、cupperといったシンプルなテーマを使用していきます。コマンドラインで、
{{< highlight Shell "linenos=false">}}
cd test/themes
{{< /highlight >}}
とthemesディレクトリに移動します。
{{< highlight Shell "linenos=false">}}
git clone https://github.com/zwbetz-gh/cupper-hugo-theme.git
{{< /highlight >}}
として、git上から拾ってきます。

## 設定ファイル編集

先ほど、git clone してきたテーマを利用するために、設定ファイルの記述を行います。設定ファイルは、test/config.tomlです。これを開くと、
{{< highlight Shell "linenos=false">}}
baseURL = "http://example.org/"
languageCode = "en-us"
title = "My New Hugo Site"

{{< /highlight >}}
となっています。これを、
{{< highlight Shell "linenos=false">}}
baseURL = "http://localhost:1313/"
languageCode = "jp"
title = "My New Hugo Site"
theme = "cupper-hugo-theme"

{{< /highlight >}}
と、変更します。それぞれの設定項目は以下のようです。

- baseURL：サイトのURL（今回の場合は、ローカル環境での動作環境を行うため上記設定）
- languageCode：デフォルト言語
- title：サイトタイトル
- theme：使用するテーマ名（/themese/ディレクトリに存在するフォルダ名）

## 新しいページ生成

さて、使用するテーマまで設定することができたので、新しいページを生成していきたいと思います。
コマンドラインで、
{{< highlight Shell "linenos=false">}}
cd test
{{< /highlight >}}
とtestディレクトリに移動し、
{{< highlight Shell "linenos=false">}}
hugo new test.md
{{< /highlight >}}

と入力します。すると、**/test/content/** に **test.md**といったファイルが生成されます。このファイルを開くと、

{{< highlight markdown  "linenos=false">}}
---
title: "Test"
date: 2020-05-15T00:32:24+09:00
draft: true
---

{{< /highlight >}}
となっています。この下に、下記のように入力してみます。
{{< highlight markdown  "linenos=false">}}
---
title: "Test"
date: 2020-05-15T00:32:24+09:00
draft: false
---

## これはテストです

ページ中のコンテンツはこの様に表示されます。

{{< /highlight >}}
保存したのち、コマンドラインに下記のコマンドを入力します。
{{< highlight Shell "linenos=false">}}
hugo server
{{< /highlight >}}
そして、[http://localhost:1313/test/](http://localhost:1313/test/) にアクセスします。すると、下記画像のように投稿が反映されたことが分かります！
{{< figure src="/img/post/hugo/hugo-testPage.JPG" title="アクセスした様子">}}

## 静的なページ生成

先述の部分で、ローカル環境での確認ができたので続いて、Web上に公開するためにhtmlやcssを生成する方法を記述していきます。コマンドラインで/test/ディレクトリ上にて、
{{< highlight Shell "linenos=false">}}
hugo
{{< /highlight >}}
と、入力します。すると... **/test/public/** といったディレクトリが生成されます。この中に、**index.html** や **/test/index.html**(先ほど示したtestページ)が生成されました！

以上で、htmlの生成まで出来たのでapache2やnginxを使ってサーバ上にファイルを置いて閲覧することができるようになったかと思います。

## 最後に

次回(近いうちに…)、Hugoを使ったテンプレートページでの開発のお話を書いていきたいと思います。

## 参考

1. Hugoでのテーマ追加方法：[https://qiita.com/yakimeron/items/42d537374abde5517267](https://qiita.com/yakimeron/items/42d537374abde5517267)
