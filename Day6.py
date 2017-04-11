#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 高级特性：切片，迭代，列表生成器，生成器，迭代器
from collections import Iterable
from collections import Iterator
import  os


def main():
    # 切片
    l = []
    for i in range(100):
        l.append(i)
    print l
    print l[0:3]
    print l[-2]

    n = list(range(50))
    print n[:10]
    print n[-10:]
    print n[-56:2]
    print n[:20:3]
    print n[::2]

    s = set(n)
    print s
    t = (n)
    print t[:10]
    print (0, 1, 2, 3, 4, 5)[:3]

    print 'ABCDEFG'[3:]

    # 迭代

    d = {'a': 1, 'b': 2, 'c': 3}
    print d
    for key in d:
        print key
    for value in d.values():
        print value

    print isinstance('abc', Iterable)
    print isinstance(d, Iterable)
    print isinstance(l, Iterable)
    print isinstance(s, Iterable)

    # 带下标的迭代
    for i, value in enumerate(l):
        print i, value

    # 列表生成式
    print [x * x for x in range(1, 11)]
    print [x * x for x in range(1, 11) if x % 2 == 0]
    print [m + n for m in 'ABC' for n in 'XYZ']
    print [m + n for m in ['a', 'b', 'c'] for n in ('x', 'y', 'z')]
    print [d for d in os.listdir(".")]
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    print [k + '=' + v for k, v in d.items()]

    print (x * x for x in range(1, 11))

    o = odd()
    next(o)
    next(o)
    next(o)

    # 迭代器
    ll = [x * x for x in range(1, 11)]
    print ll
    print type(ll)
    print isinstance([x * x for x in range(1, 11)], Iterator)
    print isinstance([],  Iterator)
    print isinstance([], Iterable)
    print isinstance({}, Iterator)
    print isinstance('abc', Iterator)
    print '********************'
    print isinstance(iter([]), Iterable)
    print isinstance(iter({}), Iterator)
    print isinstance(iter('abc'), Iterator)

    return


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


if __name__ == '__main__':
    main()