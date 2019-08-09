#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date       : 2019-08-05 16:47:24
# @Author     : caryangBingo
# @Filename   : consts.py
# @Version    : Version 1.0


"""
接口全局变量

"""

# 接口环境配置
API_ENVIRONMENT_DEBUG = 'debug'
API_ENVIRONMENT_RELEASE = 'release'

# excel文件读取配置
ROWS_CUT = 4  # 参数行截取
COLS_CUT = 3  # 参数列截取
CASE_SIG = 1  # 占位符截取
API_ATTR = {'priority': 'A2', 'tags': 'B2',
            'apipath': 'C2', 'method': 'D2', 'summary': 'E2', 'args': 'F2'}
