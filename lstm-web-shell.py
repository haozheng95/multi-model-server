#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: lstm-web-shell.py
@time: 2020-01-10 17:00
"""
import subprocess
import sys

__mtime__ = '2020-01-10'


def run():
    param_1 = sys.argv[1]
    param_2 = sys.argv[2]
    site = sys.argv[3]
    shell = "curl -o result.csv -X POST  -F 'param_1=@" + param_1 + "' -F 'param_2=@" + param_2 + "' http://47.105.165.164:7089/lstm/" + site + ""
    print(shell)
    print("param_1=", param_1)
    print("param_2=", param_2)
    print("site   =", site)
    subprocess.check_output(shell, shell=True)


if __name__ == '__main__':
    run()
