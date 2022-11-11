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

甲本健太

---
# Rustとは



---
# 今回紹介するコマンドたち

- `find`→`fd`
- `grep`→`ripgrep`
- `ls`→`exa`
- `cat`→`bat`


---
# `find` → `fd`（ファイルを探す）

- 高速！
  `README.md`（7569個）を計測
    `find`：8.0 sec
    `fd`：0.75 sec

- みやすい！
  デフォルトで色付けあり

- 賢い！
  デフォルトで`.gitignore`を無視


---
![bg 80%](./images/find.png)
![bg 80%](./images/fd.png)


---
# `grep` → `ripgrep`

- 100倍程度高速！
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

- みやすい！
  デフォルトで色付けあり
- かわいい！
  絵文字を設定できる:smile:

---
![bg 90%](./images/ls.png)
![bg 90%](./images/exa.png)


---
# `cat` → `bat`

