#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: test.py
@time: 2020-01-13 15:31
"""
import subprocess

__mtime__ = '2020-01-13'

if __name__ == '__main__':
    shell = "ls"
    output = subprocess.Popen(shell, shell=True, stdout=subprocess.PIPE)
    print(output.pid)
    # print(output.stdout.read())
