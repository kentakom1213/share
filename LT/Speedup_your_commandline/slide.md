---
marp: true
theme: dracula
footer: "[@kentakom1213](https://github.com/kentakom1213/)"
---

<!--
  class: title
-->

## うわっ…私のコマンド、遅すぎ…？
#### Rust再実装コマンドでターミナルをもっと便利に

ぱうえる（甲本健太）

---
# Rustとは



---
# 今回紹介するコマンドたち

<!-- - `find` → `fd`：ファイルを探す
- `grep` → `ripgrep`：ファイルを検索する
- `ls` → `exa`：ディレクトリの中を見る
- `cat` → `bat`：ファイルの中を見る -->

| 前 | 後 | コマンドの意味 |
| :-: | :-: | :- |
| find | fd | ファイルを探す |
| grep | ripgrep | ファイルの中身を検索する |
| ls | exa | ディレクトリの中を見る |
| cat | bat | ファイルの中を見る |

---
# `find` → `fd`
ファイルを探す

- **高速！**
  `README.md`（7569個）を計測
    `find`：8.0 sec
    `fd`：0.75 sec

- デフォルトで色付けあり
- デフォルトで`.gitignore`を無視


---
![bg 80%](./images/find.png)
![bg 80%](./images/fd.png)


---
# `grep` → `ripgrep`
ファイルの中身を検索する

- **100倍程度高速！**
  1434ファイルの中から`"アルゴリズム"`という文字列を検索
  `grep`：0.062 sec
  `ripgrep`：3.8 sec

- みやすい！

---
## `grep`コマンド
![h:500](./images/grep.png)

<!-- _footer: "" -->

---
## `ripgrep`コマンド
![h:500](images/ripgrep.png)

<!-- _footer: "" -->

---
# `ls` → `exa`
ディレクトリの中を表示する

- デフォルトで色付けあり
- 絵文字を設定できる:smile:
- tree形式でも表示できる

---
![bg 90%](./images/ls.png)
![bg 90%](./images/exa.png)


---
# `cat` → `bat`
ファイルの中身を表示する

- まるでエディタのようにファイルを見れるコマンド
- デフォルトでシンタックスハイライトあり

---
![bg 70%](./images/cat.png)
![bg 70%](./images/bat.png)

