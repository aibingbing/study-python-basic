#!/usr/bin/env python
# -*- coding:utf-8 -*-
# list and tuple


def main():
    names = ['jjj', 'ddd', 'ggg']
    names.append('77777')
    print names
    names.pop()
    print names
    names.pop(0)
    print names

    t = ('a', 'b')
    print t

    t = ('a', 'b', ['A','B'])
    print t

    t[2][0] = 'X'
    t[2][1] = 'Y'
    print t

    for name in names:
        print name

    sum = 0;
    for x in range(101):
        sum += x
    print sum

    s = 0
    n = 100
    while n > 0:
        s += n
        n -= 1
    print s



    return


if __name__ == '__main__':
    main()