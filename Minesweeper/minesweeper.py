import string
import random
import time
from functools import wraps


##### Field #####
class Field:
    """フィールドクラス
    インスタンス変数
    -----------------------------------
    h       :(縦)      ~99
    w       :(横)      ~52 (a-z, A-Z)
    mine    :(地雷の数) ~h * w
    field   :フィールドを表す二次元配列
    answer  :答えを表す二次元配列
    mask    :ゲーム中に表示する二次元配列
    mine_xy :地雷の座標、(0~8:周囲の地雷の数, 9:地雷)
    AROUND  :マスの上下左右、斜めの8方向を示す相対座標
    -----------------------------------
    """

    def __init__(self, h, w, mine):
        if h > 99 or w > 52 or mine > h * w:
            raise ValueError("\n  h :(縦) ~99\n  w :(横) ~52 (a-z, A-Z)\n  mine :(地雷の数) ~h * w")

        self.h, self.w = h, w  # フィールドの縦、横
        self.mine = mine  # 地雷の数
        self.field = [[0 for _ in range(w)] for _ in range(h)]  # フィールド
        self.answer = [[0 for _ in range(w)] for _ in range(h)]  # 正解
        self.mask = [[" " for _ in range(w)] for _ in range(h)]  # 表示用
        self.mine_xy = []  # 地雷の座標を保存

        self.AROUND = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    def is_in_field(self, x, y):
        """与えられた(x, y)がフィールドのなかにあるかどうかをチェックする"""
        if 0 <= x < self.h and 0 <= y < self.w:
            return True
        return False

    def check_xy(func):
        """与えられた(x, y)が正しい値かどうかをチェック
        他の関数をラップすることで、引数をチェックする"""
        @wraps(func)
        def inner(inst, x, y, *other):
            if not inst.is_in_field(x, y):
                raise ValueError("Coordinate out of the field.")
            return func(inst, x, y, *other)
        return inner

    @check_xy  # wrapper
    def set_mines(self, x, y):
        """地雷の座標をセットする
        与えられた(x, y)の座標には地雷を配置しない設定"""
        first_open = self.w * x + y
        flatten = list(range(first_open)) + list(range(first_open+1, self.h * self.w))  # フィールドを一次元に展開
        mine_num = random.sample(flatten, self.mine)  # ランダムに地雷を配置
        self.mine_xy = [(num//self.w, num%self.w) for num in mine_num]  # 座標の形に直す

        # フィールドに格納
        for x, y in self.mine_xy:
            self.field[x][y] = 9  # mine: 9
            self.answer[x][y] = "*"  # mine: *

    @check_xy
    def around(self, x, y):
        """与えたマスの周りのマスを返す"""
        around_cells = []
        for diff_x, diff_y in self.AROUND:
            x_, y_ = x + diff_x, y + diff_y
            if self.is_in_field(x_, y_):
                around_cells.append((x_, y_))
        return around_cells        

    @check_xy
    def count_adjasent_mines(self, x, y):
        """マスの周囲にある地雷の数をカウント"""
        around_cells = self.around(x, y)
        count_mines = [self.field[x][y] for x, y in around_cells].count(9)  # 9で表された地雷の数を数える
        return count_mines
    
    def set_number(self):
        """フィールド全体の数字を初期化"""
        for x in range(self.h):
            for y in range(self.w):
                if self.field[x][y] != 9:
                    self.field[x][y] = self.answer[x][y] = self.count_adjasent_mines(x, y)

    @check_xy
    def open(self, x, y):
        """幅優先探索を用いて指定したマスの周囲を展開する
        
        Returns
        -------
        is_gameover: bool
            開いたマスが地雷だった時にTrueを返す、その他の場合はFalseを返す
        """
        queue = [(x, y)]  # 周囲のマス
        already = []  # すでに探索済み

        while queue:
            pos = x, y = queue.pop(0)
            if pos in already:
                continue
            else:
                already.append(pos)

            cell = self.field[x][y]
            # マスが0だったとき -> 周囲のマスも開く
            if cell == 0:
                queue += self.around(x, y)
                self.mask[x][y] = 0
            # マスが数字だったとき -> 終了
            elif 1 <= cell <= 8:
                self.mask[x][y] = cell
            # マスが地雷だったとき -> Trueを返す
            else:
                self.mask[x][y] = "*"
                return True
        return False

    def is_cleared(self):
        """クリアできたかどうかをチェックする

        Returns
        -------
        is_cleared: bool
            開いていないマスが全て地雷(9)だった場合にTrueを返し、その他の場合はFalseを返す
        """
        for x in range(self.h):
            for y in range(self.w):
                mask_status = self.mask[x][y]
                field_status = self.field[x][y]
                if mask_status == " " and field_status != 9:
                    return False
        return True

    @staticmethod
    def show(array):
        """二次元配列を整形して表示する"""
        w = len(array[0])
        print("   ", *string.ascii_letters[0:w], sep=" ")

        for i, row in enumerate(array):
            # print(f"{i+1:2}|", *row, sep=" ")
            print(f"{i+1:2}|", " ".join(map(str, row)), f"|{i+1:2}")

        print("   ", *string.ascii_letters[0:w], sep=" ")
###### ######




def start(field):
    """ゲームの初期設定を行う関数"""
    field.show(field.mask)  # 最初にフィールドを表示

    while True:
        cmd = input("> ").split()
        
        if cmd == []:
            continue
        elif cmd[0] == "q":
            return
        
        try:
            x_ = int(cmd[0]) - 1
            y_ = string.ascii_letters.index(cmd[1])
            break
        except:
            continue  # エラーの場合は最初の入力を繰り返す
            
    field.set_mines(x_, y_)  # 地雷を設定
    field.set_number()  # 地雷周りの数字を設定
    field.open(x_, y_)  # 最初の座標を開く

    if field.is_cleared():
        print("\nHahahahahahaha!")
        return

    # 表示
    print()
    field.show(field.mask)

    interpret(field)  # 入力画面に戻す


def interpret(field):
    """入力を解釈する関数、同時に計測を行う"""
    start = time.time()  # タイマーをリセット

    while True:
        cmd = input("> ").split()
        
        if cmd == []:
            continue
        elif cmd[0] == "q":
            return
        
        try:
            x = int(cmd[0]) - 1
            y = string.ascii_letters.index(cmd[1])

            # field.open関数を実行、戻り値を受け取る
            is_gameover = field.open(x, y)
            is_clear = field.is_cleared()

            # フィールドを表示
            print()
            field.show(field.mask)

        except:
            continue

        # ゲームが終わるかを判定
        if is_gameover:
            print("\n!!! Game Over !!!\n")
            print("[正解]".center(field.w * 2 + 2))
            field.show(field.answer)
            print()
            return

        elif is_clear:
            print("\nCongratulations!")
            seconds = time.time() - start  # タイマーをストップ
            print(f"記録：{seconds:.2f}秒\n")
            return



if __name__ == "__main__":

    while True:
        # 初期設定
        config = input("縦 横 地雷の数\n> ").split()

        if config:
            try:
                HEIGHT, WIDTH, MINES = list( map(int, config) )
                break
            except:
                continue
        else:
            HEIGHT = WIDTH = MINES = 10
            break
    
    print(f"縦: {HEIGHT}, 横: {WIDTH}, 地雷: {MINES}個\n")

    myField = Field(HEIGHT, WIDTH, MINES)

    start(myField)  # ゲームを実行