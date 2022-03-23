import random


# oneliner-merge-sort
def merge_sort(arr):
    return arr if (la:=len(arr)) <= 1 \
        else None if (l := merge_sort(arr[:la//2])) \
                     and (r := merge_sort(arr[la//2:])) \
                     and False \
        else [l.pop(0) if l and r and l[0] <= r[0] else (r.pop(0) if r else l.pop(0))
              for _ in range(la)]


if __name__ == "__main__":
    l = [random.randint(0, 100) for _ in range(100)]
    print(l)
    print(merge_sort(l))
