import concurrent.futures

# グローバル変数の保持
variables = {}

# 標準ライブラリ関数
def print_output(value):
    print(value)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# ユーザー定義関数を格納する辞書
user_functions = {}

# エラーハンドリング用関数
def try_except(block, catch_block):
    try:
        block()
    except Exception as e:
        catch_block(e)

# ユーザー定義関数の登録
def define_function(name, func):
    user_functions[name] = func

# コマンド実行
def execute(command):
    global variables

    # コマンドを分解
    tokens = command.split()
    
    if len(tokens) == 0:
        return

    # PRINT命令
    if tokens[0] == 'PRINT':
        value = " ".join(tokens[1:])
        print_output(value)
    
    # SET命令（変数への代入）
    elif tokens[0] == 'SET':
        var_name = tokens[1]
        value = " ".join(tokens[2:])
        variables[var_name] = value
    
    # ADD命令（加算）
    elif tokens[0] == 'ADD':
        a = int(tokens[1])
        b = int(tokens[2])
        result = add(a, b)
        print_output(result)
    
    # SUB命令（引き算）
    elif tokens[0] == 'SUB':
        a = int(tokens[1])
        b = int(tokens[2])
        result = subtract(a, b)
        print_output(result)
    
    # ユーザー定義関数
    elif tokens[0] in user_functions:
        function = user_functions[tokens[0]]
        args = [int(arg) for arg in tokens[1:]]
        result = function(*args)
        print_output(result)

    else:
        print(f"Unknown command: {tokens[0]}")

# サンプルコード：ユーザー定義関数の使用
def main():
    define_function('multiply', lambda x, y: x * y)

    commands = [
        "SET var1 10",
        "PRINT var1",
        "ADD 5 3",
        "SUB 7 4",
        "multiply 2 3",  # ユーザー定義関数の呼び出し
    ]

    for command in commands:
        execute(command)

# 実行部分
if __name__ == "__main__":
    main()
