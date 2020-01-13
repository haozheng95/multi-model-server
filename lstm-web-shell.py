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
import time

__mtime__ = '2020-01-10'

BaseUrl = "http://47.105.165.164:7089"


def run():
    operation = sys.argv[1]
    shell = ""
    if operation == '-reset' or operation == '-r':
        site = sys.argv[2]
        shell = "curl -o result.csv -X GET " + BaseUrl + "/reset/" + site

    elif operation == '-prediction' or operation == '-p':
        param_1 = sys.argv[3]
        param_2 = sys.argv[4]
        site = sys.argv[2]
        shell = "curl -o result.csv -X POST  -F 'param_1=@" + param_1 + "' -F 'param_2=@" + param_2 + "' " + BaseUrl + "/lstm/" + site
        print(shell)
        print("param_1=", param_1)
        print("param_2=", param_2)
        print("site   =", site)

    else:
        print('Error 2')
        print('Unknow operation ', operation)
        exit(1)
    subprocess.check_output(shell, shell=True)
    with open("result.csv", "r") as file:
        for line in file.readlines():
            if line.startswith("Error"):
                print(line)
            elif line.startswith("Success"):
                print(line)
            return


if __name__ == '__main__':
    try:

        run()
    except KeyboardInterrupt:
        site = sys.argv[2]
        shell = "curl -X GET " + "http://47.105.165.164:7088" + "/kill/" + site
        print(shell)
        subprocess.check_output(shell, shell=True)
        time.sleep(3)
        print("kill :", site)
