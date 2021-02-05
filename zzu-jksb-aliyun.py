# -*- coding: utf-8 -*-
import re
import requests
import logging

def jksb():
    headers = {'x-forwarded-for': '本地IP'}
    resp1 = requests.post('https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login', headers=headers,
                          data={'uid': '学号', 'upw': '密码'}).text
    id = re.search(
        r'parent.window.location=\"https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first6\?ptopid=(.*?)&sid=(.*?)\"', resp1)
    resp2 = requests.post('https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb', headers=headers, data={'day6': 'b',
                                                                                      'did': '1',
                                                                                      'door': '',
                                                                                      'men6': 'a',
                                                                                      'ptopid': id.group(1),
                                                                                      'sid': id.group(2)})

    resp3 = requests.post('https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb', headers=headers, data={'myvs_1': '否',
                                                                                      'myvs_2': '否',
                                                                                      'myvs_3': '否',
                                                                                      'myvs_4': '否',
                                                                                      'myvs_5': '否',
                                                                                      'myvs_6': '否',
                                                                                      'myvs_7': '否',
                                                                                      'myvs_8': '否',
                                                                                      'myvs_9': '否',
                                                                                      'myvs_10': '否',
                                                                                      'myvs_11': '否',
                                                                                      'myvs_12': '否',
                                                                                      'myvs_13a': '41',
                                                                                      'myvs_13b': '4101',
                                                                                      'myvs_13c': '河南省郑州市',
                                                                                      'myvs_14': '否',
                                                                                      'myvs_14b': '',
                                                                                      'memo22': '成功获取',
                                                                                      'did': '2',
                                                                                      'door': '',
                                                                                      'day6': 'b',
                                                                                      'men6': 'a',
                                                                                      'sheng6': '',
                                                                                      'shi6': '',
                                                                                      'fun3': '',
                                                                                      'jingdu': '经度 6位数字',
                                                                                      'weidu': '纬度 6位数字',
                                                                                      'ptopid': id.group(1),
                                                                                      'sid': id.group(2)})
    resp3.encoding='utf-8'
    return resp3.text


def handler(event, context):
    logger = logging.getLogger()
    result=jksb()
    logger.info(result)
    return result
