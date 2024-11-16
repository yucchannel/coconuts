import re
import threading

# グローバル変数
variables = {}

# 基本的なコマンドと関数
def execute_line(line):
    line = line.strip()

    # コメント行を無視
    if line.startswith("#") or line == "":
        return

    # print コマンドの処理
    if line.startswith("print"):
        content = line[5:].strip()
        # 文字列を表示
        if content.startswith('"') and content.endswith('"'):
            print(content[1:-1])
        # 変数を表示
        elif content in variables:
            print(variables[content])
        else:
            print(f"Unknown content: {content}")

    # 変数の代入処理
    elif "=" in line:
        var_name, value = line.split("=", 1)
        var_name = var_name.strip()
        value = value.strip()

        # 数字や文字列をそのまま代入
        if value.isdigit():
            variables[var_name] = int(value)
        elif value.startswith('"') and value.endswith('"'):
            variables[var_name] = value[1:-1]
        else:
            variables[var_name] = value

    # 関数呼び出しの処理
    elif line.startswith("func"):
        func_name = re.match(r"func (\w+)\(", line).group(1)
        execute_function(func_name)

# 関数を定義して呼び出す
def execute_function(func_name):
    if func_name == "start":
        print("Function start executed!")

# マルチスレッドで並列処理をするためのスレッド
def run_multithreaded(func_name):
    thread = threading.Thread(target=execute_function, args=(func_name,))
    thread.start()

# サンプルプログラム
program = """
# Coconuts Sample Program ver 2.0

# 変数を設定
var1 = 5
var2 = "Hello"
var3 = 10

# 結果を表示
print var1
print var2

# 関数を呼び出し
func start

# マルチスレッドで関数を実行
run_multithreaded('start')
"""

# プログラムを実行する関数
def run_program(program):
    lines = program.split("\n")
    for line in lines:
        execute_line(line)

# プログラムを実行
run_program(program)
