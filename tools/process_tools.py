#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: process_tools.py
@time: 2020-01-13 15:39
"""
import subprocess

__mtime__ = '2020-01-13'


def hold_process(popen, site):
    with open("tmp/" + site, "w") as f:
        f.write(str(popen.pid))


def kill_process(site):
    with open("tmp/" + site, "r") as f:
        pid = f.read()
    shell = "kill " + str(pid)
    print("kill shell ---> ", shell)
    subprocess.Popen(shell, shell=True, stdout=subprocess.PIPE)
