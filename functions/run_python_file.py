import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        valid_pathway = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir

        if not valid_pathway:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python3", abs_file_path]

        if args:
            command.extend(args)
    
        output = subprocess.run(command, capture_output=True, text=True, timeout=30)
        exit_code = output.returncode
        stdout = output.stdout
        stderr = output.stderr
    
        result = []

        if exit_code != 0:
            result.append(f"Process exited with code {exit_code}")
        if stdout:
            result.append(f"STDOUT: {stdout}")
        if stderr:
            result.append(f"STDERR: {stderr}")
        if not stdout and not stderr:
            result.append("No ouput produced")
        return result

    except Exception as e:
        return f"ERROR: {e}"
