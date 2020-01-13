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

"""
-p 01 /root/multi-model-server/data/param-1_42.csv /root/multi-model-server/data/param-2_42.csv

/root/lstm/python/run.sh -p 01 /root/multi-model-server/data/param-1_42.csv /root/multi-model-server/data/param-2_42.csv

ps -ef | grep '-p 01 /root/multi-model-server/data/param-1_42.csv /root/multi-model-server/data/param-2_42.csv' | grep -v grep | awk '{print $2}'
"""
if __name__ == '__main__':
    shell = "ls"
    output = subprocess.Popen(shell, shell=True, stdout=subprocess.PIPE)
    print(output.pid)
    # print(output.stdout.read())
