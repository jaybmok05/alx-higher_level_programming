#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv

    def add_arg(argv):
        args_len = len(argv) - 1
        add = 0

        if args_len == 0:
            print(args_len)
            return

        for i in range(1, args_len+1):
            add += int(argv[i])

        print(add)


add_arg(argv)
