# !/usr/bin/env python3 
# -*- coding: UTF-8 -*-
"""
@project  : PyCharm
@File     : wsgi.py
@Author   : jun.zhu
@Date     : 2022/1/15 6:00 PM
@Desc     :
"""
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from watchlist import app