#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: process_tools.py
@time: 2020-01-13 15:39
"""
import os
import subprocess

__mtime__ = '2020-01-13'


def hold_process(output, site):
    # shell = "ps -ef | grep '" + shell + "' | grep -v grep | awk '{print $2}'"
    # print("shell")
    # output = subprocess.Popen(shell, shell=True, stdout=subprocess.PIPE)
    with open("tmp/" + site, "w") as f:
        f.write(str(output.pid))


def kill_process(site):
    if os.path.exists("tmp/" + site):
        with open("tmp/" + site, "r") as f:
            pid = f.read()
        # for pid in file.split("\n"):
        shell = "sudo kill -9 " + str(int(pid) + 2)
        print("kill shell ---> ", shell)
        subprocess.Popen(shell, shell=True, stdout=subprocess.PIPE)
        os.remove("tmp/" + site)
