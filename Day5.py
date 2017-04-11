#!/usr/bin/env python
# -*- coding:utf-8 -*-
# define function and variable transfer


def main():
    print my_abs(-4)
    # print my_abs('A')
    print type('A')
    nop()

    print my_power(2, 5)
    print my_power(2)
    return


def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def my_power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


def nop():
    pass


if __name__ == '__main__':
    main()