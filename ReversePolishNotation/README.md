# RPN(ReversePolishNotation) モジュール

逆ポーランド記法の勉強のために作成したプログラムです。故にそれ以外の部分は結構適当な実装。

## 基本的な使い方
**注意**：式は項ごとにスペースで区切る  
`"1+11*2*(12-3)"`　→　`"1 + 11 * 2 * ( 12 - 3 )"`

計算機を定義
```python
# RPN.py をカレントディレクトリに配置
import RPN

formula1 = "1 + 1 + 1 * 1 + 1 + 1"

calc1 = RPN.Calculator()
print( calc1.evaluate(formula1) )
# => 5.0


new_operators1 = [
  {"*": 0, "/": 0},
  {"+": 0, "-": 0}
]
calc2 = RPN.Calculator(new_operators1)  # "+", "-" と "*", "/"　の優先順位を逆転
print( calc2.evaluate(formula1) )
# => 9.0


new_operators2 = [
  {"+": 0, "-": 0},
  {"*": 0, "/": 0, "%": (lambda a, b: a % b)},
  {"|": (lambda a, b: max(a, b))}
]
calc3 = RPN.Calculator(new_operators2)
formula2 = "1 + 2 | 6 / 2"

print( calc3.evaluate(formula2) )
# => 4.0
```

コンソール

```python
# コンソールを表示
calc2.console()
# > 1 + 1 * 1 + 1
# 4.0
```

  