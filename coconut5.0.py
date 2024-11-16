# Coconut Interpreter Ver 5.0
import concurrent.futures

class CoconutInterpreter:
    def __init__(self):
        self.variables = {}

    def execute(self, code):
        # Basic command handling
        code_lines = code.split("\n")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(self._process_line, code_lines))
        return results

    def _process_line(self, line):
        line = line.strip().upper()
        if line.startswith("PRINT "):
            self.print_statement(line[6:])
        elif line.startswith("SET "):
            self.set_variable(line[4:])
        elif line.startswith("ADD "):
            self.add_variables(line[4:])
        else:
            return f"Unknown command: {line}"

    def print_statement(self, content):
        print(content)

    def set_variable(self, line):
        var_name, value = line.split("=")
        self.variables[var_name.strip()] = int(value.strip())

    def add_variables(self, line):
        var1, var2 = line.split("+")
        try:
            result = self.variables.get(var1.strip(), 0) + self.variables.get(var2.strip(), 0)
            print(result)
        except Exception as e:
            return f"Error in ADD operation: {e}"
