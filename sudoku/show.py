"""
数独の盤面をフォーマットして表示する
"""

from ploblems import problems as pb

def str2arr(s):
    nums = list(map(int, s.split()))
    arr = [nums[i:i+9] for i in range(0, 81, 9)]

    #     "| 0 0 0 | 0 0 0 | 0 0 0 |"
    sep = "+-------+-------+-------+"
    tmp = "| {} | {} | {} |"

    res = "\n".join(tmp.format(*arr[i][:3], *arr[i][3:6], *arr[i][6:9]) for i in range(9))

    return res

if __name__ == "__main__":
    print(str2arr(pb[0]))
