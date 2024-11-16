import concurrent.futures
import re

# Coconut Ver1.0FASTer Interpreter Class
class CoconutInterpreterFASTer:
    def __init__(self):
        self.variables = {}

    def execute(self, code):
        """Main function to execute Coconut code."""
        lines = code.strip().split("\n")
        threads = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for line in lines:
                line = line.strip()
                if line.startswith("PRINT"):
                    # Multithreading print statements
                    threads.append(executor.submit(self.handle_print, line))
                elif line.startswith("SET"):
                    self.handle_set(line)
                elif line.startswith("ADD"):
                    self.handle_add(line)
                elif line.startswith("MULTI"):
                    # Example of multithreaded operation
                    threads.append(executor.submit(self.handle_multi, line))
                elif line.startswith("END"):
                    break
                else:
                    print(f"Unknown command: {line}")

        # Wait for all threads to complete
        concurrent.futures.wait(threads)

    def handle_print(self, line):
        """Handle the PRINT command."""
        value = line[5:].strip()
        if value.startswith('"') and value.endswith('"'):
            print(value[1:-1])
        elif value in self.variables:
            print(self.variables[value])
        else:
            print(f"Unknown variable or text: {value}")

    def handle_set(self, line):
        """Handle the SET command."""
        match = re.match(r"SET (\w+) (\d+)", line)
        if match:
            var, value = match.groups()
            self.variables[var] = int(value)

    def handle_add(self, line):
        """Handle the ADD command."""
        match = re.match(r"ADD (\w+) (\d+)", line)
        if match:
            var, value = match.groups()
            if var in self.variables:
                self.variables[var] += int(value)

    def handle_multi(self, line):
        """Handle MULTI as a computationally expensive task."""
        match = re.match(r"MULTI (\w+) (\d+)", line)
        if match:
            var, value = match.groups()
            if var in self.variables:
                self.variables[var] *= int(value)

# Example usage
code = """
SET X 10
SET Y 20
PRINT "Starting Coconut Ver1.0FASTer"
ADD X 15
PRINT X
MULTI Y 5
PRINT Y
END
"""

interpreter = CoconutInterpreterFASTer()
interpreter.execute(code)
