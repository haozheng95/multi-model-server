#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: error-tools.py
@time: 2020-01-13 11:48
"""

__mtime__ = '2020-01-13'


def check_command_stdout(command_stdout):
    output = command_stdout.decode("utf-8")
    split = output.split("\n")
    i = 0
    for row in split:
        if "Error" in row:
            return False, row + split[i + 1]
        i += 1
    return True,
