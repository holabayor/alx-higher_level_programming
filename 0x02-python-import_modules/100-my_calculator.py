#!/usr/bin/python3

def calculate(a, op, b):
    if op == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif op == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif op == '':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif op == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operator: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    calculate(a, op, b)
