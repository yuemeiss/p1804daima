#!/usr/bin/env python
# coding=utf-8
#format格式化输出
s1 = 'I am {0}, age {1}'.format('hexm', 18)
print(s1) #I am hexm, age 18
s2 = 'I am {0}, age {1}'.format(*['hexm', 18])
print(s2) #I am hexm, age 18
s3 = 'I am {name}, age {age}'.format(name='hexm', age=18)
print(s3) #I am hexm, age 18
s4 = 'I am {name}, age {age}'.format(**{'name': 'hexm', 'age': 18})
print(s4) #I am hexm, age 18
