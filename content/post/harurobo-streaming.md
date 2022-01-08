---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "春ロボコン（関西大会）2021 ストリーミング配信に関して"
subtitle: "学生ロボコン運営における配信システムに関して関して"
summary: "学生団体が外部で配信イベントを開催するにあたっての手法に関して"
authors: [HidetoNiwa]
tags: [関西春ロボコン,ロボコン,ロボコン運営,YouTube配信]
categories: [関西春ロボコン,ロボコン,ロボコン運営,YouTube配信]
date: 2022-01-7T00:15:10+09:00
lastmod: 2022-01-7T00:15:10+09:00
featured: false
draft: false

card_image: "card/post/harurobo-streaming.png"
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

どうもです、どと～ることにゎ～んです。昨年3/12に京都府南丹市園部町にて、「春ロボコン2021（関西大会）」が開催されました。

私は、運営委員会代表として参加しつつ配信を担当していました。その時の知見も含めてメモがてら書き記していこうかとおもいます。(記事投稿が遅くなり、今更..感もありますがぜひご覧ください)

## 環境

今回、使用したデスクトップ環境を下記に示します。

- Windows 10
- CPU：Intel Core i7-3770K@3.50GHz
- RAM：16GB
- GPU：NVIDIA GeForce GTX1060 6GB

CPUはIvy Bridgeですが，i7のパワーで殴ってる（？）感じですね．GPUも搭載したデスクトップで今回は臨みました。

## 構成

続いて、システム構成のお話を書いていきます。今回の配信では、[OBS Studio](https://obsproject.com/ja)を用いて、

複数カメラのコネクションやテロップ出し、YouTubeへのストリーミング設定を行いました。その時の配信構成の概要を下記に示します。

{{<figure src="/img/post/harurobo/harurobo-streaming.png" caption="配信構成" width="75%">}}

この図を見ても分かる様に、3台のPCを用い、それぞれの映像をHDMI-USBキャプチャを用いて、画面のキャプチャーを行いました。そのため、下記商品を用いました。

<iframe style="width:50%;height:360px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=hahahahahannn-22&language=ja_JP&o=9&p=8&l=as4&m=amazon&f=ifr&ref=as_ss_li_til&asins=B08LNVN7D6&linkId=bd23a1d04db1e644ef5ed02c5a0f05cf"></iframe>

2,000円ちょっとでHDMIをキャプチャーできるのはいいですね〜USBで動画入力するのでUSBカメラと同様の入力で扱えます！

使用した感じ、たまに接触不良が起きたりはしたのですが、振動で抜けないようにすれば大丈夫でした！

LTEネットワークはレンタルのポケットWi-Fiを使いました。20GB容量があるものを用いましたが、容量は非常に余裕がありました。

## 実際に運用させてみて

さて、上記の構成で[京都府南丹市あかまつの丘 西本梅](https://nishihonme.localinfo.jp/)にて、運用してみました！

当初、配信はうまく行きましたが、途中から雨が降り始めるとLTE通信が不安定になり、通信途絶して配信が止まってしまいました...

下記動画は配信の模様を再編集したものになります。ぜひご覧ください〜

<iframe width="80%" height="400" src="https://www.youtube.com/embed/__SM6BA3woo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## 反省点

はじめ、配信はうまく行っており、音飛び等発生していなかったので構成は悪くなかったです。ただ、LTE通信が途中で途絶してしまうトラブルが非常に痛かったです...

**配信するなら有線環境を用意しよう！** 録画して、配信する形式など別の方法も考えられます。（でもライブ感は残したい...）

## 最後に

春ロボコン2021（関西大会）で配信ノウハウの最低限を得ることはできました。本年3月にも、同会場で春ロボコン2022（関西大会）が開催されます。

2022年1月上旬現在、一般観客来場可能となるように準備を進めています！ぜひ、ご来場ください！

{{< tweet 1477112594905255936 >}}
