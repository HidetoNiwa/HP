---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "CubeIDEコード整形"
subtitle: "CubeIDEにおけるコード整形"
summary: "CubeIDEにおける手動整形・自動整形のお話"
authors: [HidetoNiwa]
tags: [CubeIDE,eclipse,STM32]
categories: [CubeIDE,eclipse,STM32]
date: 2020-12-29T10:55:40+09:00
lastmod: 2020-12-29T10:55:40+09:00
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
お久しぶりです，にゎ～んです．さて，今回はCubeIDEにおけるコード整形のお話を書いていきたいと思います．

## 手動整形

整形したいファイル上で，「Ctrl」+「Shift」+「f」を押します．
すると，下図のような選択が出てくるので好きな方を選んで「OK」を押します．

* そのファイル全部を行う．
* その行のみ行う．

{{< figure src="/img/post/CubeIDE/Formmating.PNG" title="コード整形選択肢" width="250px">}}

## 自動整形

ページ上部の「Window」>「Preference」をクリック.

{{< figure src="/img/post/CubeIDE/Formmating2.PNG" title="「Window」>「Preference」" width="450px">}}

Preference中の「C/C++」>「Editor」>「Save Actions」の"Format source code"にチェックを入れ，下の"Apply and Close"をクリック．

{{< figure src="/img/post/CubeIDE/Formmating3.PNG" title="「Window」>「Preference」" width="450px">}}
