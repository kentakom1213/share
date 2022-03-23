
# ワンライナー

## マージソートの実装

```python
def merge_sort(arr): return arr if len(arr) <= 1 else None if (l := merge_sort(arr[:len(arr)//2])) and (r := merge_sort(arr[len(arr)//2:])) and False else [l.pop(0) if l and r and l[0]<=r[0] else (r.pop(0) if r else l.pop(0)) for _ in range(len(arr))]
```

### 解説

展開すると以下のようになる

```python
def merge_sort(arr):

    # 再帰の終了条件
    if len(arr) <= 1:
        return arr
        
    # left, rightに分割
    l = merge_sort(arr[:len(arr)//2])
    r = merge_sort(arr[len(arr)//2:])

    # mergeする
    return [l.pop(0) if l and r and l[0]<=r[0] else (r.pop(0) if r else l.pop(0)) for _ in range(len(arr))]
```

また、mergeの操作は以下のようにワンライナーにした

```python
# mergeの原型
res = []
while l and r:
    if l[0] <= r[0]:
        res.append( l.pop(0) )
    else:
        res.append( r.pop(0) )
res += l + r

# for文で書き換え
res = []
for _ in range(len(l) + len(r)):
    if l and r and l[0] <= r[0]:
        res.append( l.pop(0) )
    elif r:
        res.append( r.pop(0) )
    else:
        res.append( l.pop(0) )  # lだけに残っている場合

# 内包表記にまとめる
[l.pop(0) if l and r and l[0]<=r[0] else (r.pop(0) if r else l.pop(0)) for _ in range(len(arr))]
```

また、下のような謎の式が入っているのは

```python
None if (l := merge_sort(arr[:len(arr)//2])) and (r := merge_sort(arr[len(arr)//2:])) and False else ...
```
```python
[ ... range( len(l := merge_sort(arr[:len(arr)//2])) + len(r := merge_sort(arr[len(arr)//2:])) ) ]
```

これを書きたかったがrange関数の中でセイウチ演算子が使えなかったため、
left, rightを三項演算子の条件として評価させるため