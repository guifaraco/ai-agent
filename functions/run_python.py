import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_directory_path = os.path.abspath(working_directory)
    if not abs_path.startswith(abs_working_directory_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(["python3", file_path, *args], timeout=30, capture_output=True, text=True, cwd=abs_working_directory_path)
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f'Error: executing Python file: {e}'
