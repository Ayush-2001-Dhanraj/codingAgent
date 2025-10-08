# from functions.get_file_info import get_file_info
# from functions.get_file_contents import get_file_contents
# from functions.write_file import write_file
from functions.run_python_file import run_python_file


def main():
    # result = get_file_info("calculator")
    # print(result)

    # result = get_file_info("calculator", "pkg")
    # print(result)

    # result = get_file_info("calculator", "/bin")
    # print(result)

    # result = get_file_info("calculator", "../")
    # print(result)

    # print(get_file_contents("calculator", "pkg/calculator.py"))
    # print(get_file_contents("calculator", "hello.py"))
    # print(get_file_contents("calculator", "lorem.txt"))
    # print(get_file_contents("calculator", "main.py"))
    # print(get_file_contents("calculator", "/bin/cat"))

    # print(write_file("calculator", "lorem.txt", "Hello World"))
    # print(write_file("calculator", "new.txt", "Hello World"))
    # print(write_file("calculator", "pkg2/new.txt", "Hello World"))
    # print(write_file("calculator", "/bin/new.txt", "Hello World"))

    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    # print(run_python_file("calculator", "tests.py"))
    # print(run_python_file("calculator", "../main.py"))
    # print(run_python_file("calculator", "nonexistant.py"))


main()
