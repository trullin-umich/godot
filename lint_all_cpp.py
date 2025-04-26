import os
import subprocess

# automatic linter for all c++ files
def should_lint(file_path):
    return file_path.endswith('.cpp') and 'thirdparty' not in file_path

def lint_cpp_files(root_directory):
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if should_lint(file_path):
                print(f"Linting {file_path}")
                subprocess.run(["cpplint", file_path])

if __name__ == "__main__":
    lint_cpp_files(".")