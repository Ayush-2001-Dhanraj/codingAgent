import os
from config import MAX_CHARS
from google.genai import types


def get_file_contents(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: '{file_path}' is not a  file inside '{working_directory}'"
    if not os.path.isfile(abs_file_path):
        return f"Error: '{file_path}' is not a file"

    file_content_string = ""
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += (
                    f'[...file "{file_path}" truncated at {MAX_CHARS} characters...]'
                )
        return file_content_string
    except Exception as e:
        return f"Error: Exception reading file '{file_path}': {e}"


schema_get_file_contents = types.FunctionDeclaration(
    name="get_file_contents",
    description="Gets the content of a file as string, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file, from the working directory to read.",
            ),
        },
    ),
)
