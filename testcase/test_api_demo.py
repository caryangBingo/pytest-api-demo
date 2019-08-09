#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date       : 2019-07-30 09:54:56
# @Author     : caryangBingo
# @Filename   : example.py
# @Version    : Version 1.0

import io
import os
import sys
import requests
import pysnooper
import allure
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.assertpy import assert_that, fail
from common.excel import OrthogonalCaseProcessing
from config.config_docs import getConfig
from common.requestspy import Requestpy


#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

baseUrl = getConfig("debug_test", "baseUrl")
CaseAttrData = OrthogonalCaseProcessing()

worksheet = CaseAttrData.getWorksheets()

api_baseUrl = '{}'.format(baseUrl)
headers = {
    "Accept":
    "application/json;charset=UTF-8",
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
}
priority = CaseAttrData.readAttributes(worksheet).get('priority')
tags = CaseAttrData.readAttributes(worksheet).get('tags')
apipath = CaseAttrData.readAttributes(worksheet).get('apipath')
method = CaseAttrData.readAttributes(worksheet).get('method')
summary = CaseAttrData.readAttributes(worksheet).get('summary')
args = CaseAttrData.readAttributes(worksheet).get('args')


# http://devmsmobapi.lanmang.me/api/EnterpriseQueryMobile/GetEnterpriseById?entId=1042&uid=20165943


class TestCaseExecuting():
    """docstring for TestCaseExecuting"""

    @allure.step
    @pytest.mark.parametrize('params_exp', [data for data in CaseAttrData.readWorkslData(worksheet)])
    def test_api_request(self, params_exp):
        # print(params)
        paramsValue, expextValue = params_exp[0], params_exp[1]
        #print(params, exp)
        resp_result = Requestpy.request_exec(self, method=method, url=api_baseUrl + apipath,
                                             params=paramsValue, headers=headers)
        # elapsedTime = r.elapsed.total_seconds()
        # assertEqual(r.status_code, http_statusCode)
        print(resp_result)
        # assert_that(resp_result['responsesBody'].get(
        #    'status_code')).is_equal_to(expextValue.get('http_statusCode'))
        assert_that(resp_result['responsesBody'].get(
            'code')).is_equal_to(expextValue.get('code'))
        """
        try:
            assert_that(resp_result['responsesBody'].get(
                'code')).is_equal_to(0)
        except AssertionError:
            assert_that(resp_result['responsesBody'].get(
                'code')).is_equal_to(-1)
        """
        # assert Assertions.assert_msg(
        #    result['message'], responsesBody['message'])
        # assert Assertions.assert_body(
        #    result['bodyMessage'], responsesBody['bodyMessage'])
        # assert Assertions.assert_subCode(
        #    result['subCode'], responsesBody['subCode']
