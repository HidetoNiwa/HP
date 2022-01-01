---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Hugo Shortcode"
subtitle: ""
summary: ""
authors: [HidetoNiwa]
tags: [Hugo]
categories: [Hugo]
date: 2020-05-15T16:40:00+09:00
lastmod: 2020-05-15T16:40:00+09:00
featured: false
draft: false

card_image: "card/pages/hugo-shortcode.png"
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

このページでは、Hugoでよく使われるShortCodeについて書いて行きます。

## figure

\{\{\< figure src="/img/pages/hugo-shortcode/avatar.jpg" title="画像投稿サンプル" width="150px"\>\}\}

### 出力例

{{< figure src="/img/pages/hugo-shortcode/avatar.jpg" title="画像投稿サンプル"  width="150px">}}

### パラメータ

#### src

/static/以下のファイルパス

#### title

画像につけるタイトル

### width

画像幅(px,%で指定可能)

<!--## High
-->
## 参考

1. shortcodeに関する公式リファレンス：[https://gohugo.io/content-management/shortcodes/](https://gohugo.io/content-management/shortcodes/)
