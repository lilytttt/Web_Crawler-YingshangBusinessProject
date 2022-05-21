#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 20:53:59 2022

@author: ttlily
"""

import json
import requests
import pandas as pd
def project_list_collect (i):
    postUrl = 'http://www.winshangdata.com/wsapi/project/list3_5'
    # payloadData数据
    payloadData = {
     'orderBy': "1",
     'pageNum': i,
     'pageSize': 60
    }
    # 请求头设置
    payloadHeader = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'appType': 'bigdata',
        'Connection': 'keep-alive',
        'Content-Length': '160',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': '_uab_collina=164993574180695922772105; Hm_lvt_f48055ef4cefec1b8213086004a7b78d=1649935743; JSESSIONID=7C3AA105338636F375AF9856DA416CB9; Hm_lpvt_f48055ef4cefec1b8213086004a7b78d=1649935808',
        'Host': 'www.winshangdata.com',
        'Origin': 'http://www.winshangdata.com',
        'platform': 'pc',
        'Referer': 'http://www.winshangdata.com/projectList',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
        'uuid': '123456'
    }


    dumpJsonData = json.dumps(payloadData)
    #print(f"dumpJsonData = {dumpJsonData}")
    res = requests.post(postUrl, data=dumpJsonData, headers=payloadHeader )
    res.json()
    if res.status_code==200: 
        total_projects = res.json()['data']['total']
        content = res.json()['data']['list']
        df = pd.json_normalize(content)
        
        return [total_projects, df]
    else:
        return ['error', 'error']