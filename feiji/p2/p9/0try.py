#!/usr/bin/env python
# coding=utf-8
import time
try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            print(content)
            if len(content)==0:
                break
            time.sleep(2)
    except Exception as bug:
        # 如果在读取文件的过程中，产生了异常，那么就会捕获到
        # 比如按下了　ctrl + c
        print('bug是:%s'%bug)

    finally:
        f.close()
        print('关闭文件')
except:
    print('没有这个文件')
