---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "git コマンド集"
subtitle: "なにかと使うgitのコマンド集"
summary: "なにかと使うgitのコマンド集"
authors: [HidetoNiwa]
tags: [git,command,GitHub]
categories: [git,command,GitHub]
date: 2021-09-23T00:43:38+09:00
lastmod: 2021-09-23T00:43:38+09:00
featured: false
draft: false

card_image: "card/pages/git-command.png"
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

[GitHub](https://github.com/)など、ソースコード管理でよく使われるgit。

Visual Studio CodeなどでGUIでgitを使うこともできますが、やはり細かい操作はコマンドラインでしたいですよね！（実際に筆者はそう思っています。）

そのコマンドラインでの備忘録として、まとめています。使うコマンドが増えれば追記していきます（たぶん）

## clone系

```bash
git clone <URL> <cloneするフォルダ名>
```

## branch系

### ローカルのbranch名変更

```bash
git branch -m <古いブランチ名> <新しいブランチ名>
```

## add系

gitで次にcommitするファイルの追加

```bash
git add -A #全てのファイルの場合
```

## commit系

### コミットメッセージ付けてcommit

```bash
git commit -m "（コミットメッセージ）"
```

## push系

オンラインサーバへpush

### originサーバへbranchを追加

```bash
git push --set-upstream origin <branch名>
```

### originサーバへpush

```bash
git push
```
