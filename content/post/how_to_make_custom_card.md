---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Twitterカードの作り方"
subtitle: "Hugoで記事別にTwitterカードを作る方法"
summary: ""
authors: [HidetoNiwa]
tags: [Hugo,Twitter]
categories: [Hugo,Twitter]
date: 2022-01-02T07:24:03Z
lastmod: 2022-01-02T07:24:03Z
featured: false
draft: false

card_image: "card/post/how_to_make_custom_card.png"
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
お久しぶりです。どと〜ること、にゎ〜んです。先日、このブログにページごとのTwitterカード画像を生成して適用させることができるようになったと、Tweetしました。このページではその方法に関して説明していきたいと思います。

{{< tweet user="hahahahaha_NNN" id="1477264343045574656" >}}

### 環境
今回使用した環境は下記に列挙する環境です。version等揃える必要なない（と思う）ですが、この環境で作ってたんだーくらいは感じてください。

- Hugo Extended
- GitHub Pages
- Python3.8

## Twitterカードとは？

先述のTweetの様に、Twitterにリンクを共有した際に、リンクが画像として表示される機能です。

<メリット>
- Twitter上で画像でリンクが出るのでクリックされやすい

<デメリット>
- クライアント側でTweetを見たときに画像を取得するので、データ通信量/サーバへの負荷がかかる？（多分）

まぁ、圧倒的にメリット＞デメリットなので設定したほうがいいですね。

## 実装

では、いざ実装しましょう。下記のような順番で実装を行っていきます。
- 画像生成
  - 画像へブログ名＆記事名追加
- 画像を記事に適用
- 記事からカードを適用

これらの処理には、一部の界隈で嫌われがちなPythonを用いました。（Python3.8）
Pythonを利用した理由は、

- 画像処理等の実装がライブラリを使って行うので楽
- Windows,UbuntuなどOS間の互換性が高い

と感じたからです。

<details>
<summary><a href="https://github.com/HidetoNiwa/HP/blob/master/python/make-card-pic.py">実装したコード</a>（Python）</summary>
<script src="https://gist.github.com/HidetoNiwa/1e0f7220cc8f4ddc4dd90d090d108622.js" data-gist-line="1-20"></script>
</details>

### ベース画像の準備

まずは、カードのベースとなる画像を用意します。今回は下記の画像を用いました。

{{< figure src="https://github.com/HidetoNiwa/HP/blob/master/python/card.png?raw=true" title="ベース画像">}}

### 記事一覧を取得

記事一覧の取得を行うため、/content/以下のディレクトリの取得を行いました。また、記事ではないページのmarkdownの取得を行わないため、別途ignoreリストを作成して、除外しました。

また、Python標準ライブラリである、globを用いているのでimportします。

```Python
import glob

ignore_list = {"./content/privacy.md", "./content/terms.md","./content/authors/niwa/_index.md","./content/home/about.md","./content/home/index.md","./content/home/posts.md","./content/home/skills.md","./content/post/_index.md","./content/publication/_index.md","./content/talk/_index.md"}

def get_dir():
    path = './content/**/*.md'
    file_list = glob.glob(path, recursive=True)
    file_list = list(filter(lambda x: x not in ignore_list, file_list))
    return file_list
```

### 記事からのタイトル取得

記事からタイトルの取得を行うため、前に取得した記事リストから順にファイルオープンを行い記事のタイトルの抽出を行いました。

```Python
def get_title(file_path):
    print("Open file...", file_path)

    f = open(file_path, 'r', encoding="utf-8")  # File Open（文字コード指定）
    datalist = f.readlines()
    f.close()
    title_string = "title: "

    for i in range(len(datalist)):
        text = datalist[i]
        title = text.split('"')
        if title[0] == title_string:
            break
    print(title)
    return title[1]
```

### カード画像に文字入れ

カード中に文字を入れるため、Pillowと呼ばれるPythonの画像ライブラリを用いました。これは、Pythonのライブラリとなるので、入っていない場合は下記コマンドで入れます。

```bash
pip3 install Pillow
```

このPillowを用いて、画像中に文字を入れています。文字のフォントは[Google Fonts](https://fonts.google.com/)のものを利用させていただきました。

今回の関数では、フォント、画像ファイル、文字列、（文字を入れる）x座標、y座標、フォントサイズ、文字色を引数として扱っています。

```Python
from PIL import Image, ImageDraw, ImageFont
def make_image(font_path, img_path, text, x=0.0, y=0.0, font_size=32, font_color="black"):
    font = ImageFont.truetype(font_path, font_size)
    img = Image.open(img_path)

    img_d = ImageDraw.Draw(img)
    text_size = img_d.textsize(text, font)  # テキストサイズの取得

    img_d.text((x-(text_size[0]/2), y-(text_size[1]/2)),
               text, fill=font_color, font=font)
    img.save(img_path)
```

### 記事タイトル文字数取得

記事タイトルが長すぎると、Twitterカード上の収まりが悪くなってしまいます。そのことを防ぐため、全角文字7文字以上で、

文字サイズが小さくなるようにしました。その際、文字カウントを行ったのが下記コードになります。その際、UnicodedataといったPythonの標準ライブラリを用いてます。

```Python
import unicodedata
def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count
```

### 記事にカード画像をリンク

Hugoでは、最初の方に"---"で囲まれた部分があります。そこを、Front Matterと呼びます。

このFront Matterと呼ばれる部分に、カード画像の保存場所を明記していきます。

今回は、"card_image:"の後ろにカードのディレクトリを追記する形にしています。

また、すでに記載されているかどうかの判定も行っています。（2重で記載するの防ぐため）

```Python
def add_card_info(file_path,card_path):
    f = open(file_path, 'r', encoding="utf-8")  # File Open（文字コード指定）
    datalist = f.readlines()
    f.close()

    card_path = card_path[13:]
    img_string = "card_image:"
    section_string = "---"

    start_formatter = False
    img_info = False

    for i in range(len(datalist)):
        text = datalist[i][:11]
        if text == img_string:
            img_info = True
            break
        text = text[:3]
        if text == section_string:
            if start_formatter:
                break
            else:
                start_formatter=True
    
    card_info = img_string + " " + '"'+card_path+'"\n'
    if img_info:
        datalist[i]=card_info
    else:
        datalist.insert(14,card_info)

    f = open(file_path, 'w', encoding="utf-8")  # File Open（文字コード指定）
    f.writelines(datalist)
    f.close()
    return text
```

### Hugo Themeに適用

さて、ここまでで、画像の生成・画像と記事の紐づけができました。最後は、HTMLにこのカードを紐づけましょう。

自分が用いているテーマ（academic）では、これらの情報は /layouts/partials/site_head.htmlに記載されていました。
> 基本的には<head>タグ内に書けば大丈夫です。

実際に、カード画像を指定しているのは下記HTML文になります。つまりは、ここに画像が適用されれば良いです。
```HTML
<meta property="og:image" content="{{.}}">
<meta property="twitter:image" content="{{.}}">
```

自分の環境では、$og_imageにうまいこと代入されれば良い感じでした。そこで下記のように編集しました。

isset .Params "card_image"：これは、"card_image"が記事中で設定されていますよといった意味になります。

そして、.Params.card_imageで記事から保存場所を引っ張ってきています。

```GO
{{ else if isset .Params "card_image" }}<!--Twitterカード等に用いられる画像があるかの判定、Front Matter-->
  {{ $og_image = printf "img/%s" .Params.card_image | absURL }}
```

## Python動作

さて、これでPythonを動作させて画像の生成・記事へファイルのリンクを行えば大丈夫です。Pythonファイルを、/python/make-card-pic.pyに保存しました。

このファイルを実行するために、Hugoのトップディレクトリで下記コマンドを実行すれば自動で画像を生成してくれます！

```bash
python3 ./python/make-card-pic.py
```

## 最後に

この記事を書いていたら思ったよりも長くなってしまいました。まぁ、これ関連のコード作成も研究等の兼ね合いから、1年くらいしてた気がします。

現状、ローカルで画像を生成してコミットする形となってしまっているのが欠点です。また、記事のMarkDownがリネームされると対応できません。

Draft（下書き）状態の記事にも画像を生成してしまいます...これらを踏まえると、下記の機能を実装したいですね。

- GitHub Actionsで記事がGitHub Pagesに公開されるときに同時にカード画像が生成されるようにする
- 使用されていない画像が無いか確認する
- Title取得時にDraftかどうかの判定を行う

最後まで読んでくれてありがとうございました！
