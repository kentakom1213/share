---
marp: true
---

## フローチャートを作ろう！
# Mermaid入門

---
# Mermaidってなに？
- Markdownの中に簡単なコードだけで図を埋め込めるツールです
- [mermaid.live](https://mermaid.live) $\leftarrow$ お試し用

![](images/mermaid.png)

---
# どんな図が作れるの？
![bg right:50%](images/figs.png)

- フローチャート
- シーケンス図
- ガントチャート
- クラス図 / ER図
- GitGraph
- パイチャート

などなど...

出典: https://mermaid-js.github.io


---
# メリット・デメリット

## メリット
- 全て文字列で表現される！
    - あらゆるエディタで編集できる
    - データの共有が楽
    - gitで管理できる
- 手書きよりも綺麗

## デメリット
- 細かい調整が難しい
  (ノードの配置など)

---
# 具体的に、どんなコードになってるの？
- フローチャート
- GitGraph
- ER図

---
## フローチャート
![bg right:28%](images/graph.png)

```
graph LR
    A --> B
    C(C) --> D{中身}
    E --0--> F
    E --1--> G
```

---
## GitGraph
```
gitGraph
    commit
    commit
    branch development
    commit
    commit
    checkout main
    commit
    merge development
    commit
```
![](images/gitgraph.png)

---
## ER図
![bg right:30%](./images/ER.png)

```
erDiagram
    Courses ||--o{ Resources : ""

    Courses {
        int id
        int course_id
        string course_name
        int status
    }

    Resources {
        int course_id
        string resourse_name
        int size_mb
    }
```

---
# 参考
- [Mermaid Documentation](https://mermaid-js.github.io/mermaid/#/)
- [MermaidでER図のスケッチをしたら簡単すぎて衝撃だった](https://zenn.dev/kyohei_shibuya/articles/0cafee2a1c1651)