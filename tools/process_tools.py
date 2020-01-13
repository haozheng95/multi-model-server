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


def hold_process(site, shell):
    shell = "ps -ef | grep '" + shell + "' | grep -v grep | awk '{print $2}'"
    output = subprocess.Popen(shell, shell=True, stdout=subprocess.PIPE)
    with open("tmp/" + site, "w") as f:
        f.write(output.stdout.read().decode("utf-8"))


def kill_process(site):
    with open("tmp/" + site, "r") as f:
        file = f.read()
    for pid in file.split("\n"):
        shell = "sudo kill -9 " + str(pid)
        # shell = "./kill.sh " + str(pid)
        print("kill shell ---> ", shell)
        subprocess.Popen(shell, shell=True, stdout=subprocess.PIPE)
    os.remove("tmp/" + site)
