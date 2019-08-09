#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date       : 2019-07-04 19:16:51
# @Author     : caryangBingo
# @Filename   : config_docs.py
# @Version    : Version 1.0

import io
import os
import sys
import configparser as cparser

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

_base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_base_dir = _base_dir.replace('\\', '/')

config_path = _base_dir + "/config/config_docs.ini"

conf = cparser.ConfigParser()
conf.read(config_path, encoding='utf-8')


def getConfig(arg1, arg2):
    _Url = conf.get(arg1, arg2)
    return _Url
