#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date       : 2019-08-06 09:47:38
# @Author     : caryangBingo
# @Filename   : deploy-run.py
# @Version    : Version 1.0

import io
import os
import sys
import pytest
import subprocess
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

_base_dir = str(os.path.dirname(os.path.abspath(__file__)))
_base_dir = _base_dir.replace('\\', '/')


class Shell:

    @staticmethod
    def invoke(cmd):
        stdout, stderr = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='D:/Program Files/allure/bin').communicate()
        output = stdout.decode('gbk')
        print(output)
        return output


if __name__ == '__main__':

    shell = Shell()

    xml_reportPath = _base_dir + '/resource/report'
    allure_reportPath = _base_dir + '/resource/allure-report'

    _shellargs = ['-s', '-q', '--alluredir', xml_reportPath]
    _args_argv = sys.argv[1:]
    pytest.main(args=_shellargs)

    _cmd = 'allure generate {0} -o {1} --clean'.format(
        xml_reportPath, allure_reportPath)

    try:
        shell.invoke(_cmd)
    except Exception:
        raise
