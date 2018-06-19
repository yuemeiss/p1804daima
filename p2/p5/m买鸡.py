#!/usr/bin/env python
# coding=utf-8
li = []
for i in range(1, 100 // 5):
    for x in range(1, 100 // 3):
        for y in range(1, 100 * 3):
            if i + x + y == 100 and i * 5 + x * 3 + y / 3 == 100:
                print(i, x, y)
