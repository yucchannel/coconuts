import concurrent.futures

class CoconutInterpreter:
    def __init__(self):
        self.variables = {}
        self.commands = {
            'PRINT': self.print_command,
            'SET': self.set_command,
            'ADD': self.add_command,
            'MULTIPLY': self.multiply_command,
            'DIVIDE': self.divide_command
        }
        self.thread_executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    def print_command(self, args):
        print(" ".join(args))

    def set_command(self, args):
        var_name, value = args[0], int(args[1])
        self.variables[var_name] = value

    def add_command(self, args):
        var_name, value = args[0], int(args[1])
        if var_name in self.variables:
            self.variables[var_name] += value
            print(f"{var_name} is now {self.variables[var_name]}")
        else:
            print(f"{var_name} not set yet")

    def multiply_command(self, args):
        var_name, value = args[0], int(args[1])
        if var_name in self.variables:
            self.variables[var_name] *= value
            print(f"{var_name} is now {self.variables[var_name]}")
        else:
            print(f"{var_name} not set yet")

    def divide_command(self, args):
        var_name, value = args[0], int(args[1])
        if var_name in self.variables:
            if value != 0:
                self.variables[var_name] /= value
                print(f"{var_name} is now {self.variables[var_name]}")
            else:
                print("Error: Division by zero")
        else:
            print(f"{var_name} not set yet")

    def execute(self, command_line):
        parts = command_line.split()
        command = parts[0]
        args = parts[1:]

        if command in self.commands:
            self.thread_executor.submit(self.commands[command], args)

    def run(self, program):
        for line in program:
            self.execute(line)

# Example usage:
if __name__ == "__main__":
    interpreter = CoconutInterpreter()
    program = [
        "SET x 10",
        "ADD x 5",
        "MULTIPLY x 3",
        "DIVIDE x 4",
        "PRINT x"
    ]
    interpreter.run(program)
