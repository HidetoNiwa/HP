---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "BroadFiler"
subtitle: ""
summary: "タブ機能付きファイラー（BroadFiler）のインストールと使ってみた、ちょこっとの感想"
authors: [HidetoNiwa]
tags: [WIndws,ファイラー,BroadFiler]
categories: [Windows,ファイラー,BroadFiler]
date: 2020-05-12T00:00:17+09:00
lastmod: 2020-05-12T00:00:17+09:00
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
# はじめに
こんにちは！どと～ることにゎ～んです。さて、皆さんはWindowsを日ごろ使用しているかと思います。（Macユーザ/Ubuntu(Linux)ユーザもいらっしゃるかと思いますが、本記事はWindowsユーザ向け記事です...）

しかし、Windowsのデフォルトのファイルソフト（ファイラー）である、Windows Explorer ですが、作業を進めていくうちにWindow数が多くなっていき、**自分がどのフォルダを開いているか分からなくなる**ことが多々あるかと思います。そこで、今回は「BroadFiler」を用いて**タブ**、**グループ**を使ったファイル操作管理を行っていこうと思います。

# インストールの仕方
## インストーラーをダウンロード
まず、[ダウンロードサイト](https://www.vector.co.jp/soft/dl/winnt/util/se490120.html)にアクセスし、画面中央にある、ダウンロードページへをクリックします。

続いて、**このソフトを今すぐダウンロード**をクリックします。

すると、zip形式でインストーラーをダウンロードできるので、展開します。

{{< figure src="/img/post/BroadFiler/zip.JPG" title="zipファイルを展開した結果">}}

## インストーラーを実行
展開した結果、様々なファイルがありますが**steup.exe**を実行するだけで大丈夫です。（他の解凍ソフトはうまくセットアップできなかった時のものらしい）

setup.exeを実行したら、「次へ」「同意する」を押していくとセットアップできます。
{{< figure src="/img/post/BroadFiler/end-install.JPG" title="インストール完了した結果" >}}

# では、実際に実行してみましょう
それでは、実際に実行してみたいと思います。下記画像のようなアイコンが存在すると思うので実行してみます。
なお、ここで注意してほしいのは、右クリックして**管理者として実行**することです。

{{< figure src="/img/post/BroadFiler/ico.png" title="アイコン" >}}

# 感想
Windwos Explorerにはない、**タブ機能**、**グループ機能**がありその辺を欲してる人にとってはとてもありがたいソフトになってるかと思います。

{{< figure src="/img/post/BroadFiler/show.JPG" title="実行した結果" >}}

そういえば、だいぶ以前にWindows Explorerにタブ機能が実装されるという話があったのですけどどうなったんですかね...