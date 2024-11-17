import re

class CoconutInterpreterV1_1Faster:
    def __init__(self):
        self.variables = {}

    def execute(self, code):
        lines = code.strip().split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith("PRINT"):
                self.handle_print(line)
            elif line.startswith("SET"):
                self.handle_set(line)
            elif line.startswith("ADD"):
                self.handle_add(line)
            elif line.startswith("END"):
                break
            else:
                print(f"Unknown command: {line}")

    def handle_print(self, line):
        value = line[5:].strip()
        if value.startswith('"') and value.endswith('"'):
            print(value[1:-1])
        elif value in self.variables:
            print(self.variables[value])
        else:
            print(f"Unknown variable or text: {value}")

    def handle_set(self, line):
        match = re.match(r"SET (\w+) (\d+)", line)
        if match:
            var, value = match.groups()
            self.variables[var] = int(value)

    def handle_add(self, line):
        match = re.match(r"ADD (\w+) (\d+)", line)
        if match:
            var, value = match.groups()
            if var in self.variables:
                self.variables[var] += int(value)

# Example usage
if __name__ == "__main__":
    code = """
    SET X 10
    PRINT "Coconut Ver1.1Faster"
    ADD X 15
    PRINT X
    END
    """
    interpreter = CoconutInterpreterV1_1Faster()
    interpreter.execute(code)
