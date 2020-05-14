---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Hugoでの投稿の仕方"
subtitle: ""
summary: "Hugoプロジェクトの作成方法&静的なサイトの生成方法"
authors: [admin]
tags: [hugo]
categories: [hugo]
date: 2020-05-09T23:27:50+09:00
lastmod: 2020-05-09T23:27:50+09:00
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

PowerShell、Terminalなど使用OSにおけるコマンドコンソールを開き、プロジェクトを作成したいディレクトリにcdやmkdirを使用して移動します。移動した先で、
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

これでプロジェクトは完成しましたが、これではサイトとして表示されないので、テーマを導入していきたいと思います。ここでは、cupperといったシンプルな
{{< highlight Shell "linenos=false">}}
cd test/themes
{{< /highlight >}}
とthemesディレクトリに移動します。
{{< highlight Shell "linenos=false">}}
git clone https://github.com/zwbetz-gh/cupper-hugo-theme.git
{{< /highlight >}}
として、

## 新しいページ生成

それでは、新しいページを生成していきたいと思います。

{{< highlight Shell "linenos=false">}}
cd test
{{< /highlight >}}
とtestディレクトリに移動し、
{{< highlight Shell "linenos=false">}}
hugo new post/test.md
{{< /highlight >}}

と入力します。すると、**/test/content/post/** に **test.md**といったファイルが生成されます。このファイルを開くと、

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
draft: true
---

## Test

hogehoge

{{< /highlight >}}
そして、下記のコマンドを入力します。
{{< highlight Shell "linenos=false">}}
hugo server
{{< /highlight >}}
そして、[http://localhost:1313/](http://localhost:1313/) にアクセスします。

## 静的なページ生成

以上で、htmlの生成まで出来たのでapache2やnginxを使ってサーバ上にファイルを置いて閲覧することができるようになったかと思います。

## 最後に

次回(近いうちに…)、Hugoを使ったテンプレートページでの開発のお話を書いていきたいと思います。
