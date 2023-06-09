#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv

    def arg_calc(argv):
        num_args = len(argv) - 1
        a = int(argv[1]) if num_args >= 1 else 0
        op = argv[2] if num_args >= 2 else ''
        b = int(argv[3]) if num_args >= 3 else 0

        if num_args != 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            sys.exit(1)

        if op == '+':
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
        elif op == '-':
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
        elif op == '*':
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
        elif op == '/':
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)


arg_calc(argv)
