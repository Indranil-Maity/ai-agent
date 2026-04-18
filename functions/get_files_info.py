import os

def get_files_info(working_directory, directory="."):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_directory, directory))
        valid_target_dir = os.path.commonpath([abs_working_directory, target_dir]) == abs_working_directory

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        contents = os.listdir(target_dir)
        res = []
        for content in contents:
            file_path = os.path.join(target_dir, content)
            is_dir = os.path.isdir(file_path)
            file_size = os.path.getsize(file_path)
            output = f"- {content}: file_size={file_size} bytes, is_dir={is_dir}"
            res.append(output)
        return res
    except Exception as e:
        return f"Error: {e}"

