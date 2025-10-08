from functions.get_file_info import get_file_info
from functions.get_file_contents import get_file_contents


def main():
    # result = get_file_info("calculator")
    # print(result)

    # result = get_file_info("calculator", "pkg")
    # print(result)

    # result = get_file_info("calculator", "/bin")
    # print(result)

    # result = get_file_info("calculator", "../")
    # print(result)

    print(get_file_contents("calculator", "pkg/calculator.py"))
    print(get_file_contents("calculator", "hello.py"))
    print(get_file_contents("calculator", "lorem.txt"))
    print(get_file_contents("calculator", "main.py"))
    print(get_file_contents("calculator", "/bin/cat"))


main()
