from google.genai import types
from functions.get_file_info import get_file_info
from functions.get_file_contents import get_file_contents
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from config import WORKING_DIRECTORY


def function_call(function_call_part, verbose=False):
    if verbose:
        print(
            f"Calling function: {function_call_part.name} ({function_call_part.args})"
        )
    else:
        print(f"Calling function: {function_call_part.name}")

    result = ""
    if function_call_part.name == "get_file_info":
        result = get_file_info(WORKING_DIRECTORY, **function_call_part.args)
    if function_call_part.name == "get_file_contents":
        result = get_file_contents(WORKING_DIRECTORY, **function_call_part.args)
    if function_call_part.name == "write_file":
        result = write_file(WORKING_DIRECTORY, **function_call_part.args)
    if function_call_part.name == "run_python_file":
        result = run_python_file(WORKING_DIRECTORY, **function_call_part.args)

    if result == "":
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function {function_call_part.name}"},
                )
            ],
        )

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )
