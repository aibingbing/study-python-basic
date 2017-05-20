# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
 study third party library:requests
'''

import requests


def main():
    '''doc string
    '''

    r = requests.get(' https://exmail.qq.com/login', auth=('aibingbing@etutech.com', 'Etuabb2017'))
    # print r.status_code
    # print r.headers['content-type']
    # print r.encoding
    # print r.text

    r = requests.get('http://www.betterbing.net')
    print r.text
    print r.encoding


if __name__ == '__main__':
    main()
