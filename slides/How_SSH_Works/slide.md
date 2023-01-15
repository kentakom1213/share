---
marp: true
header: "SSHの仕組み"
footer: "2023/01/16 NUOCW"
theme: dracula
paginate: true
---


<!--
headingDivider: 2
_class: title
_paginate: false
-->

# SSHの仕組み

サーバサイド班　<a style="color:white; text-decoration: none;" href="https://github.com/kentakom1213">甲本健太 :link:</a>


## 目次




## SSHとは

SSHとは**Secure Shell**（安全なシェル）の略称であり、安全にリモートコンピュータと接続するためのプロトコル。

- サーバに接続して作業するときなどに利用する

![h:300](images/about_ssh.png)


## SSH接続が成立するまでの流れ

1. クライアントによるサーバの認証
2. セッションキーの生成
3. サーバによるクライアントの認証


## SSH接続時のログ出力

`ssh`コマンドに`-v`オプションをつけると接続の際のログを確認できる

![h:400](images/ssh_log.png)


## 認証方法

- パスワード認証
- 公開鍵認証

## 公開鍵暗号の種類

- RSA
  - 素因数分解ベースの暗号
- ECDSA
  - 楕円関数上での離散対数問題


## 参考

- Secure Shell (Wikipedia)
  https://ja.wikipedia.org/wiki/Secure_Shell
- OpenSSH (公式)
  https://www.openssh.com/
- Understanding SSH Workflow
  https://medium.com/@hellomudit/understanding-ssh-workflow-66a0e8d4bf65

