#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date       : 2019-08-07 10:23:08
# @Author     : caryangBingo
# @Filename   : requestspy.py
# @Version    : Version 1.0

import io
import os
import sys
import random
import requests
#from requests_toolbelt import MultipartEncoder


class Requestpy(object):

    def __init__(self):
        """
        :param env:
        """
        self.headers = {
            "Accept": "application/json;charset=UTF-8",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
        }

    def request_exec(self, method, url, params, headers):
        if method == 'get':
            return Requestpy.get_request(self, url, params, headers)
        else:
            pass

    def get_request(self, url, params, headers):
        """
        Get请求
        :param url:
        :param param:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if params is None:
                resp = requests.get(
                    url=url, headers=headers)
            else:
                resp = requests.get(
                    url=url, params=params, headers=headers)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = resp.elapsed.microseconds / 1000
        time_total = resp.elapsed.total_seconds()

        resp_dicts = dict()
        resp_dicts['status_code'] = resp.status_code
        try:
            resp_dicts['responsesBody'] = resp.json()
        except Exception as e:
            print(e)
            resp_dicts['responsesBody'] = ''
        #response_dicts['text'] = response.text
        resp_dicts['time_consuming'] = time_consuming
        resp_dicts['time_total'] = time_total

        # print(resp_dicts)
        return resp_dicts

    def post_request(self, url, data, header):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(
                    url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.post(
                    url=url, params=data, headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts
    '''
    def post_request_multipart(self, url, data, header, file_parm, file, f_type):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param type:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(
                    url=url, headers=header, cookies=self.get_session)
            else:
                data[file_parm] = os.path.basename(
                    file), open(file, 'rb'), f_type

                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' +
                    str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                response = requests.post(
                    url=url, params=data, headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts
    '''

    def put_request(self, url, data, header):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.put(
                    url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.put(
                    url=url, params=data, headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts


"""
if __name__ == '__main__':
    requests = Requestpy(
        'get', 'http://devmsmobapi.lanmang.me/api/EnterpriseQueryMobile/GetEnterpriseById', {"entId": 1042, "uid": 20165943})
"""
