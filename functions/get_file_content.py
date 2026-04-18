import os

def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        valid_path = os.path.commonpath([abs_working_dir, target_file_path]) == abs_working_dir

        if not valid_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file_path) as f:
            file_content = f.read(10000)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} at characters]'

        return file_content


    except Exception as e:
        return f"ERROR: {e}"
