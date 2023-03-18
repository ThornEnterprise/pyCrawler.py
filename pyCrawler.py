import os

def read_from(py_list):
    py_dict = {}
    for i, item in enumerate(py_list):
        print(f' {i} : {item}')
        py_dict[i] = item
    try:
        user_input = int(input("Please select which corresponding number to read file from : "))
        if user_input in py_dict.keys():
            print(py_dict[user_input])
            with open(py_dict[user_input], 'r') as file:
                for line in file:
                    print(line, end='')
    except Exception as error:
        print(f'Error : {error}')


def init():
    py_list = []
    print(os.uname().sysname)
    os.chdir('..')
    os.chdir('..')
    os.chdir('..')
    dir = os.getcwd()
    print(dir)

    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            print(f'    {os.path.join(root, name)}')
            if name.endswith(".py") and not name.startswith('._'):
                py_list.append(f'{os.path.join(root, name)}')

        for name in dirs:
            print(os.path.join(root, name))

    print()
    print('------' * 3)
    print()
    return py_list

def main():
    py_list = init()
    while True:
        read_from(py_list)
        user_input = input('\n\n\nAny Key to Continue, "exit" to Quit : ').lower()
        if user_input == 'exit':
            break

if __name__ == '__main__':
    main()