# !/usr/bin/env python3 
# -*- coding: UTF-8 -*-
"""
@project  : PyCharm
@File     : errors.py
@Author   : jun.zhu
@Date     : 2022/1/15 4:57 PM
@Desc     :
"""
from flask import render_template

from watchlist import app


@app.errorhandler(400)
def bad_request(e):
    return render_template('errors/400.html'), 400


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500