#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: app.py
@time: 2020-01-03 16:23
"""
import os
import subprocess

__mtime__ = '2020-01-03'

from flask import Flask, request, Response
from flask_uploads import UploadSet, DATA, configure_uploads, ALL

app = Flask(__name__)
app.config['UPLOADED_PHOTO_DEST'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
app.config['UPLOADED_PHOTO_ALLOW'] = DATA

photos = UploadSet('PHOTO')

configure_uploads(app, photos)


@app.route("/lstm/<site>", methods=["POST"])
def lstm(site):
    # shell = "python /root/lstm/python/main.py 0 12"
    param_1 = photos.save(request.files['param_1'])
    param_2 = photos.save(request.files['param_2'])
    param_1_path = photos.path(param_1)
    param_2_path = photos.path(param_2)
    shell = "/root/lstm/python/run.sh " + site + " " + param_1_path + " " + param_2_path
    # output = subprocess.check_output(shell, shell=True)
    file_path = "/root/lstm/python/" + site + "results.csv"

    def generate():
        if not os.path.exists(file_path):
            raise ("File not found.")
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(chunk_size=10 * 1024 * 1024)
                if not chunk:
                    break
                yield chunk

    return Response(generate(), content_type="application/octet-stream")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=7089, threaded=False)
