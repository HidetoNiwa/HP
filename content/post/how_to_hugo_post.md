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

PowerShell、Terminalなど使用OSにおけるコマンドコンソールを開き、プロジェクトを作成したいディレクトリにcdやmkdirを使用して移動します。
移動した先で、
{{< highlight Shell "linenos=false,hl_lines=8 15-17">}}
hugo new site test
{{< /highlight >}}
と実行します。すると、そのディレクトリに、**test**といったフォルダが作成されます。続いて、

{{< highlight Shell "linenos=false,hl_lines=8 15-17">}}
cd test
{{< /highlight >}}
とtestディレクトリに移動し、
{{< highlight Shell "linenos=false,hl_lines=8 15-17">}}
hugo server
{{< /highlight >}}

## 静的なページ生成

以上で、htmlの生成まで出来たのでapache2やnginxを使ってサーバ上にファイルを置いて閲覧することができるようになったかと思います。

## 最後に

次回(近いうちに…)、Hugoを使ったテンプレートページでの開発のお話を書いていきたいと思います。
