import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: '{file_path}' is not a  file inside '{working_directory}'"

    if not os.path.isfile(abs_file_path):
        return f"Error: '{file_path}' is not a file"

    if not file_path.endswith(".py"):
        return f"Error: '{file_path}' is not a python file"

    try:
        final_args = ["python", file_path]
        final_args.extend(args)
        output = subprocess.run(
            final_args,
            cwd=abs_working_directory,
            timeout=30,
            capture_output=True,
        )
        final_string = f"""
        STDOUT: {output.stdout}
        STDERR: {output.stderr}
        """
        if output.stderr == "" and output.stdout == "":
            final_string = "No output produced.\n"
        if output.returncode != 0:
            final_string += f"Process exited with code: {output.returncode}\n"
        return final_string
    except Exception as e:
        return f"Error: Exception running python file '{file_path}': {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file using python interpreter, Accepts additional CLI args as an optional array.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file, from the working directory to run.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An additional array of strings to be used as the CLI args for the python file.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)
