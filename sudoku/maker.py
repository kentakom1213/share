
import random
from copy import deepcopy

def random_field_maker():
    """非再帰dfs"""

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

    return None

def main():
    random.seed(0)

    for _ in range(10):
        f = random_field_maker()
        print(*f, sep="\n")
        print()


if __name__ == "__main__":
    main()