---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Hugo(Windows)セットアップ"
subtitle: ""
summary: "Windowsにおけるhugoのセットアップの仕方"
authors: [HidetoNiwa]
tags: [Hugo,Windows]
categories: [Hugo,Windows]
date: 2020-05-08T12:15:00+09:00
lastmod: 2020-05-08T12:15:00+09:00
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

こんにちは！どと～ること、にゎ～んです。さて、今日はhugoのWindowsでの環境構築のやり方について記述していきたいと思います。

## Hugoとは

導入として、Hugoの紹介。Hugoとは、「静的ファイルでサイトを作るための支援ツール」です。
他のWebページ作成ツールとして、Wordpressなどありますがこれらのサイトにはデータベース等が必要となり、保守/管理といった点からも煩雑さが目立ちます。[1]

基本的に、HugoのサイトはMarkDown（GitHubとかのReadMe.mdとか）形式で記述することができ、記述の容易性等も挙げることができるかと思います。

## Windows上でのHugoの環境構築

Windows上のhugo環境構築方法として下記の2種類を用いた方法があるそうです。[2]

- scoop
- Chocolatey

それぞれ、UbuntuやCentOSで言うところのaptやyumといったパッケージ管理ソフトだそうです。（筆者もよくわかってませんけど、できたからよし！！！）今回ではscoopを用いた方法にしてみたいと思います。

## （下準備）scoopの環境構築

それでは、下準備としてscoopの環境構築を行っていきたいと思います。
まず、PowerShellを起動します。

そして、続いて下記コマンドを実行します。

{{< highlight Shell "linenos=false,hl_lines=8 15-17" >}}
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
iwr -useb get.scoop.sh | iex
{{< / highlight >}}

以上で完了です！！！早いですね、簡単ですね、誰でもできそうですね。

### 確認方法

{{< highlight Shell "linenos=false,hl_lines=8 15-17" >}}
scoop help
{{< / highlight >}}
これで、Scoopの各種コマンドの確認ができます。

### PowerShell管理者権限に関して

サイトによっては、"管理者権限で"って記述も見られますが、Hugoの環境構築を行いたい場合は普通の状態で構いません
ってか、管理者権限で環境構築すると、管理者として今後走らせないといけない煩雑さが生まれたりもする？*要検証

## Hugoの環境構築

それでは、続いてHugoの環境構築を行っていきます。Hugoには、'''Hugo'''と'''Hugo Extended'''と2種類存在します。

特に理由がない場合は、'''Hugo Extended'''のインストールをおすすめします。（上位互換のため...）一部のテーマは、'''Hugo Extended'''でないとコンパイルできないときがあります。

インストールには下記のコマンドをPowerShellで実行すれば大丈夫です。[3]

### Hugo Extended

{{< highlight Shell "linenos=false,hl_lines=8 15-17" >}}
scoop install hugo-extended
{{< / highlight >}}

### Hugo

{{< highlight Shell "linenos=false,hl_lines=8 15-17" >}}
scoop install hugo-extended
{{< / highlight >}}

## 最後に

以上で、HugoのWindows上に環境構築する方法はおしまいです！これであなたも静的な安定したWebページライフを！

## 参考

1. <https://knowledge.sakura.ad.jp/22908/>
    - Hugoに関する紹介に使用させていただきました。
2. <https://qiita.com/Dooteeen/items/12dc8fb14042888113d0>
   - Scoopのインストール方法を参考にさせて頂きました。
3. <https://gohugo.io/getting-started/installing/>
   - hugo公式ドキュメント、windowsでの環境構築のお話が書かれている
