import random, sys


def rangeValue():
    for c in range(0,20):
        sys.stdout.write(f'{random.randint(0,1000)}\n')


if __name__ == '__main__':
    rangeValue()
