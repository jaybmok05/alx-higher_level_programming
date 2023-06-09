#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv

    def output_args(argv):

        args_len = len(argv) - 1
        index = 1

        if args_len == 0:
            print("{:d} argument.".format(args_len))
            return
        else:
            if args_len == 1:
                print("{:d} arguments:".format(args_len))
            else:
                print("{:d} arguments:".format(args_len))

            while index <= args_len:
                if argv[index].isdigit():
                    print("{:d}: {:d}".format(index, int(argv[index])))
                else:
                    print("{:d}: {:s}".format(index, argv[index]))
                index += 1


output_args(argv)
