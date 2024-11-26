#!/usr/bin/env python3

import argparse

def calc_factorial(value):
    total = 1
    while value > 0:
        total *= value
        value -= 1

    return total

def calc_fibonacci(value):
    if value <= 1:
        return value

    return calc_fibonacci(value - 1) + calc_fibonacci(value - 2)

def main(args):
    factorial = calc_factorial(args.value)
    print(f'{args.value}!: {factorial}')
    fibonacci = calc_fibonacci(args.value)
    print(f'{args.value}th fibonacci number: {fibonacci}')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('value', type=int,
                        help='The integer to use as the base integer of a factorial \
                              and to find the nth Fibonacci number')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    main(args)
