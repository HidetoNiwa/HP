---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Hugo Academicテーマの導入"
subtitle: ""
summary: "HugoでのAcademicテーマを使用したサイトの製作方法"
authors: [HidetoNiwa]
tags: [Hugo,Academic]
categories: [Hugo,Academic]
date: 2020-05-22T00:29:36+09:00
lastmod: 2020-05-22T00:29:36+09:00
featured: false
draft: false

card_image: "card/post/hugo_Academic.png"
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

こんにちは！どと～ることにゎ～んです。

これまでに、Hugoの環境構築の仕方、投稿の仕方と投稿を出してきました。

- [Windows上でのHugoの構築の仕方](https://www.hahahahaha-nnn.work/post/hugo_in_windows/)
- [Hugoでの投稿の仕方](https://www.hahahahaha-nnn.work/post/how_to_hugo_post/)

これらをもとに、今回は、HugoのAcademicテーマの導入に関して記述していきたいと思います。

## Academic テーマとは

HugoのAcademicテーマとは、数多くあるHugoのテーマの中で最もGitHub上でスターがつけられている（らしい）

実は本サイトでも採用しています。ブログと、個人/組織紹介を兼ねたWebサイトに向いています。

## Academicテーマサンプル導入

それでは、実際にAcademicテーマの導入を進めて行きたいと思います。

（以下、Hugo,gitがコマンドラインで使用可能であることを前提に話を進めていきます。）

### git clone

コマンドラインを開き、下記コマンドを入力します。

{{< highlight Shell "linenos=false">}}
git clone https://github.com/sourcethemes/academic-kickstart.git Site_name
{{< /highlight >}}

これだと、サンプル部分のみgit cloneされAcademicテーマのサブモジュール部分がcloneされないので下記コマンドを順次実行していきます。

{{< highlight Shell "linenos=false">}}
cd Site_name
git submodule update --init --recursive
{{< /highlight >}}

そしたら下記コマンドを実行してみます。

{{< highlight Shell "linenos=false">}}
hugo server
{{< /highlight >}}

ここまで、問題がなければ[http://localhost:1313/](http://localhost:1313/)にアクセスしましょう！すると下記画像のように表示されるかと思います。（大体問題になるのは、git submoduleを導入するあたりです。）

{{< figure src="/img/post/hugo/hugo-Academic.JPG" title="Academicテーマ動作結果" width="400px">}}

## 最後に

とりあえず、Academicテーマサンプルページの導入方法は以上になります。

このサンプルページをもとに、各種設定を行いGitHub Pageseとして公開をしていくのはまた後々のお話...

また、他のHugoテーマと同様にCSSや設定をカスタマイズすることが可能です！（このサイトでは、記事の表示幅、フォントをカスタマイズしています。）

気が向いたら、その辺も書いていきましょうかねぇ.。o○

## 参考

1. [Hugo + Academic テーマを使ったブログの作り方](https://qiita.com/harumaxy/items/58e7e4273c61e7e260b3)
