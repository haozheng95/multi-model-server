#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: app.py
@time: 2020-01-03 16:23
"""
import subprocess

__mtime__ = '2020-01-03'

from flask import Flask

app = Flask(__name__)


@app.route("/lstm", methods=["POST"])
def lstm():
    shell = "python /root/lstm/python/main.py 0 12"
    output = subprocess.check_output(shell, shell=True)
    return output


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=7099, threaded=False)
