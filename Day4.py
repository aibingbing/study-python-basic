#!/usr/bin/env python
# -*- coding:utf-8 -*-
# dict and set


def main():
    d = {"abb": 95, "sjp": 100}
    print d
    print '%s\'s score:%s' % ('sjp', d["sjp"])

    print d.get('sss')
    print d.items()
    print d.keys()
    print d.values()
    print d.has_key('sjp')
    print d.viewitems()
    print d.viewvalues()

    s = set([1, 2, 2, 3, 3, 4])
    print s
    s.add(5)
    print s
    s.remove(1)
    print s
    

    return


if __name__ == '__main__':
    main()