import tempfile
import subprocess
import os
import shutil


class SmplProcessor:
    def __init__(self, mode) -> None:
        self.mode = mode
        self.indentation = 0
        self.in_multiline_string = False
        self.multiline_string_content = []
        # To store the variable being assigned the multi-line string
        self.multiline_variable = None
        self.interpreted_code = ""
        self.glob = {}

    def run_file(self, file_path):
        self.process_file(file_path)

        if self.mode == "--compiler":
            return self.compile_python_string(file_path)
        elif self.mode == "--interpreter":
            return exec(self.interpreted_code, self.glob)
        elif self.mode == "--transpiler":
            return self.write_file()

    def write_file(self):
        with open('transpiled.py', 'w') as output_file:
            output_file.write(self.interpreted_code)

    def compile_python_string(self, file_path):

        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
            temp_file.write(self.interpreted_code.encode())
            temp_file_path = temp_file.name
        try:

            subprocess.run([
                "pyinstaller",
                "--onefile",
                "--name", file_path,  # Specify the output file name
                temp_file_path
            ], check=True)

            # Remove the build directory and .spec file to keep only dist
            shutil.rmtree('build')  # Remove the build directory
            spec_file = f"{file_path}.spec"
            if os.path.exists(spec_file):
                os.remove(spec_file)  # Remove the .spec file

            print(f"Compilation of {temp_file_path} complete.")
        except subprocess.CalledProcessError as e:
            print(f"Error during compilation: {e}")
        finally:

            os.remove(temp_file_path)

    def process_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                self.indentation = len(line) - len(line.lstrip())

                if not line.strip():
                    indent = '    ' * self.indentation
                    self.interpreted_code += indent + '\n'

                # Multi-line string handling (inside LET block)
                if self.in_multiline_string:
                    if '"""' in line:  # End of multi-line string
                        self.multiline_string_content.append(
                            line.strip().replace('"""', ''))
                        multi_line_string = ''.join(
                            self.multiline_string_content)
                        self.interpreted_code += f'{
                            self.multiline_variable} = """{multi_line_string}"""\n'
                        self.in_multiline_string = False
                        self.multiline_string_content = []
                        self.multiline_variable = None
                    else:
                        self.multiline_string_content.append(line)
                    continue

                if line.startswith("LET") and '"""' in line:
                    self.in_multiline_string = True
                    parts = line.split(" ", 3)
                    self.multiline_variable = parts[1]
                    self.multiline_string_content.append(line.strip().split(
                        '"""')[1])  # Capture the first part after """
                    continue

                # Process the line
                python_code = self.process_line(line.strip())
                if python_code:
                    indent = '    ' * self.indentation
                    self.interpreted_code += indent + python_code + '\n'

    def process_line(self, line):
        if line.startswith("LET"):
            return self.handle_let_statement(line)
        elif line.startswith("OUTPUT"):
            return self.handle_output_statement(line)
        elif line.startswith("IF"):
            return self.handle_if_statement(line)
        elif line.startswith("ELSE IF"):
            return self.handle_else_if_statement(line)
        elif line.startswith("ELSE"):
            return self.handle_else_statement(line)
        elif line.startswith("FUNCTION"):
            return self.handle_function_definition(line)
        elif line.startswith("USE"):
            return self.handle_global(line)
        elif line.startswith("RETURN"):
            return self.handle_return_statement(line)
        elif line.endswith(")"):  # Indicates a function call
            return self.handle_function_call(line)
        return line  # Default return for unhandled lines

    def handle_let_statement(self, line):
        parts = line.split(" ", 3)
        variable = parts[1]

        # Handle INPUT case in LET statements
        if "INPUT" in parts[3]:
            return self.handle_input_statement(parts)

        # Handle RANDOM case in LET statements
        if "RANDOM" in line:
            range_part = parts[3].split()
            start, end = int(range_part[3]), int(range_part[5])
            return f"import random\n{'    ' * self.indentation}{variable} = random.randint({start}, {end})"

        # Handle standard LET assignment
        expression = parts[3]

        if expression == "TRUE":
            return f"{variable} = True"
        elif expression == "FALSE":
            return f"{variable} = False"

        return f"{variable} = {expression}"

    def handle_input_statement(self, parts):
        variable = parts[1]
        input_type = 'str'
        if "STRING" in parts[3]:
            input_type = 'str'
        elif "INTEGER" in parts[3]:
            input_type = 'int'
        comment_start = parts[3].find('"')
        comment = parts[3][comment_start:] if comment_start != -1 else '""'

        return f'{variable} = {input_type}(input({comment}))'

    def handle_output_statement(self, line):
        parts = line.split(" ", 1)
        expression = parts[1]
        return f"print({expression})"

    def handle_if_statement(self, line):
        parts = line.split()
        variable = parts[1]
        operator = ' '.join(parts[2:5])
        condition = self.get_condition(operator, variable, parts[5])
        return f"if {condition}:"

    def handle_else_if_statement(self, line):
        parts = line.split()
        variable = parts[2]
        operator = ' '.join(parts[3:6])
        condition = self.get_condition(operator, variable, parts[6])
        return f"elif {condition}:"

    def handle_else_statement(self, line):
        return "else:"

    def handle_function_definition(self, line):
        parts = line.split(" ", 1)[1]  # Skip "FUNCTION"
        self.in_function = True
        return f"def {parts}:"

    def handle_return_statement(self, line):
        return line.replace("RETURN", "return", 1)

    def handle_global(self, line):
        parts = line.split()
        return f"global {parts[1]}"

    def handle_function_call(self, line):
        if "LET" in line:
            parts = line.split(" ", 3)
            variable = parts[1]
            function_call = parts[3]
            return f"{variable} = {function_call}"
        return line.strip()  # Keep function calls without affecting indentation

    def get_condition(self, operator, variable, value):
        if operator == "IS LESS THAN":
            return f"{variable} < {value}"
        elif operator == "IS GREATER THAN":
            return f"{variable} > {value}"
        elif operator == "IS EQUAL TO":
            return f"{variable} == {value}"
        return ""
