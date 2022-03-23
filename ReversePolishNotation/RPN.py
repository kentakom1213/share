import operator

class Calculator:
    ### default operators ###
    __default_functions = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    __default_priority =  {
        "__bottom": -1,
        ")": 0,
        "+": 1, "-": 1,
        "*": 2, "/": 2,
        "__others": 3,
        "(": 4,
    }

    def __init__(self, new_operators=None):
        """
        演算子の更新: 
        new_operators = [
            {"+": 0, "-": 0},  # 優先順位 低い
            {"*": 0, "/": 0},
            {"operator1": function1, "operator2": function2}  # 優先順位 高い
        ]
        
        演算子の定義に関数以外が与えられた場合はデフォルトの定義が反映される。（ただし "+", "-", "*", "/" のみ）
        """
        if new_operators:
            self.__functions, self.__priority = Calculator.set_operators(new_operators)
        
        else:
            self.__functions, self.__priority = self.__default_functions, self.__default_priority

    # 演算子の置き換え
    @classmethod
    def set_operators(cls, new_operators):
        new_functions = {}
        new_priority = {"__bottom": -1, ")": 0}

        for i, operators in enumerate(new_operators):
            for operator_key, operator_val in operators.items():
                # 関数の上書き
                if callable(operator_val):
                    new_functions[operator_key] = operator_val
                else:
                    new_functions[operator_key] = cls.__default_functions[operator_key]
                # 優先順位の上書き
                new_priority[operator_key] = i + 1
                new_priority["__others"] = i + 2
                new_priority["("] = i + 3

        return new_functions, new_priority

    # 演算子などの優先順位を取得、to_polishで使用
    def get_priority(self, el):
        return self.__priority.get(el, self.__priority["__others"])

    # 中置記法の文字列(スペース区切り)を逆ポーランド記法形式の文字列のリストに変換
    def to_polish(self, formula):
        formula_split = formula.split()
        formula_rv = list(reversed(formula_split))
        
        stack = ["__bottom"]
        polish = []

        while formula_rv:
            item = formula_rv.pop()

            while self.get_priority(item) <= self.get_priority(stack[-1]):
                if stack[-1] == "(":
                    if item == ")":
                        stack.pop()
                    break

                polish.append(stack.pop())

            if item != ")":
                stack.append(item)

        while len(stack) > 1:
            polish.append(stack.pop())

        return polish

    # 逆ポーランド記法形式の文字列のリストを処理、数値(float)を返す
    def parse_polish(self, polish):
        polish_rv = list(reversed(polish))
        
        stack = []
        
        while polish_rv:
            item = polish_rv.pop()
            
            if item in self.__functions.keys():
                val2, val1 = stack.pop(), stack.pop()
                stack.append(self.__functions[item](val1, val2))
            
            else:
                stack.append(float(item))
            
        return stack.pop()
    
    # 中置記法の文字列を計算
    def evaluate(self, formula):
        polish = self.to_polish(formula)
        return self.parse_polish(polish)
    
    # コンソールを表示
    def console(self):
        print("Console, \"q\" to quit")
        while True:
            command = input("> ")

            if command == "q":
                break

            print(self.evaluate(command))




if __name__ == "__main__":
    calc1 = Calculator()  # デフォルトの計算

    new_ops1 = [
        {"*": 0, "/": 0},
        {"+": 0, "-": 0},
    ]
    calc2 = Calculator(new_ops1)  # 足し算/引き算　と　掛け算/割り算　の優先順位を逆転

    new_ops2 = [
        {"+": 0, "-": 0},
        {"*": 0, "/": 0, "%": operator.mod},
        {"^": operator.pow}
    ]
    calc3 = Calculator(new_ops2)  # 演算子 ("%": あまりをもとめる, "^": 累乗) を追加

    f1 = "1 + 1 + 1 * 1 + 1 + 1"  # 数と演算子はスペース区切りで与える
    print("f1 =", f1)
    print("calc1 > ", calc1.evaluate(f1))
    print("calc2 > ", calc2.evaluate(f1))

    f2 = "1 + 2 ^ 3 % 3"
    print("f2 =", f2)
    print("calc3 > ", calc3.evaluate(f2))