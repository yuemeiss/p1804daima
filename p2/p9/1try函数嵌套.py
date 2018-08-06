#!/usr/bin/env python
# coding=utf-8
def test():
    print('=====test1-1====')
    print(num)
    print('=====test1-2====')
def test1():
    print('=====test2-1======')
    test()
    print('=====test2-2======')
def test2():
    try:
        print('===test3-1===')
        test()
        print('===test3-2===')
    except Exception as bug:
        print('bug是:%s'%bug)
    print('====test3-2====')
test2()
print('====华丽的分割线====')
test()

