import shlex


def command_ls(args):
    print("ls")
    print("Аргументы:", args)


def command_cd(args):
    print("cd")
    print("Аргументы:", args)


def parse_line(command):
    try:
        return shlex.split(command)
    except ValueError as e:
        raise ValueError("Ошибка синтаксиса (незакрытые кавычки)")


def execute(command):
    try:
        parts = parse_line(command)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return True

    if len(parts) == 0:
        return True

    name = parts[0]
    args = parts[1:]

    if name == "ls":
        command_ls(args)

    elif name == "cd":
        command_cd(args)

    elif name == "exit":
        if len(args) > 0:
            print("Ошибка: exit не принимает аргументов")
            return True
        return False

    else:
        print("Ошибка: неизвестная команда")

    return True


def main():
    vfs_name = "practice_vfs"

    while True:
        try:
            command = input(vfs_name + "> ")
            if not execute(command):
                break
        except (KeyboardInterrupt, EOFError):
            print()
            break


if __name__ == "__main__":
    main()