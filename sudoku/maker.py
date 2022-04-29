
import random
from copy import deepcopy
from collections import deque

def random_field_maker():
    """
    # ランダムなフィールド(数独の解)を求める
    - 非再帰DFSを用いる (解が求まった場合速やかに停止)
    - フィールドをランダムに埋める
    """

    arr = [[0]*9 for _ in range(9)]
    stack = [(arr, 0)]

    # 求まったとき
    while stack:
        arr, cell = stack.pop()

        if cell == 81:
            return arr

        i, j = cell//9, cell%9
        if arr[i][j] == 0:

            # 乱択で代入
            numbers = list(range(1, 10))
            random.shuffle(numbers)
            for n in numbers:

                # --- 行 ---
                if n in arr[i]:
                    continue

                # --- 列 ---
                is_in_col = False
                for r in range(9):
                    is_in_col |= arr[r][j] == n
                if is_in_col:
                    continue

                # --- ブロック ---
                is_in_block = False
                for r in range(i//3*3, i//3*3+3):
                    for c in range(j//3*3, j//3*3+3):
                        is_in_block |= arr[r][c] == n
                if is_in_block:
                    continue

                # 条件をみたしていたとき
                new = deepcopy(arr)
                new[i][j] = n
                stack.append((new, cell+1))

        else:
            stack.append((arr, cell+1))


def solve_counter(arr):
    """
    # 解として考えられる盤面の組み合わせをカウントする
    - 2を超えたら打ち切る
    """

    stack = [(arr, 0)]
    ans = 0

    # 求まったとき
    while stack:
        arr, cell = stack.pop()

        if cell == 81:
            ans += 1
            if ans > 1:
                break
            continue

        i, j = cell//9, cell%9
        if arr[i][j] == 0:

            # 乱択で代入
            numbers = list(range(1, 10))
            random.shuffle(numbers)
            for n in numbers:

                # --- 行 ---
                if n in arr[i]:
                    continue

                # --- 列 ---
                is_in_col = False
                for r in range(9):
                    is_in_col |= arr[r][j] == n
                if is_in_col:
                    continue

                # --- ブロック ---
                is_in_block = False
                for r in range(i//3*3, i//3*3+3):
                    for c in range(j//3*3, j//3*3+3):
                        is_in_block |= arr[r][c] == n
                if is_in_block:
                    continue

                # 条件をみたしていたとき
                new = deepcopy(arr)
                new[i][j] = n
                stack.append((new, cell+1))

        else:
            stack.append((arr, cell+1))
    
    return ans


def make_problem_from_field(arr, n):
    """
    # 数独の解から問題を作成する
    """
    res = deepcopy(arr)

    cells = list(range(81))
    random.shuffle(cells)
    q = deque(cells)
    seen = set()
    
    while n and q:
        cell = q.popleft()
        if cell in seen:
            print(f"{n} : can't find")
            break

        i, j = cell//9, cell%9

        if res[i][j] != 0:
            res[i][j] = 0
            if solve_counter(res) != 1:
                # もとに戻す
                res[i][j] = arr[i][j]
                seen.add(cell)
                q.append(cell)
            else:
                n -= 1

    return res


def pprint(arr):
    for row in arr:
        print(*row)


def test():
    random.seed(0)

    f = random_field_maker()
    pprint(f)
    print()

    n = int(input())
    plob = make_problem_from_field(f, n)
    pprint(plob)


if __name__ == "__main__":
    test()