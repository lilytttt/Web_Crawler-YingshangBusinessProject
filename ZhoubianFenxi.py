#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 20:43:32 2022

@author: ttlily
"""

import pandas as pd
import json
import requests

def zhoubian_fenxi (uid, pwd, id_list): 
    # 请求头设置
    payloadHeader = {    
        'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'appType': 'bigdata',
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJleHBpclwiOjE2NTI1MzYxMDA1MTQsXCJ1aWRcIjpcImV2YXpoYWlcIixcInV1aWRcIjpcIjEyMzQ1NlwifSIsImlhdCI6MTY0OTk0NDEwMH0.5xpvKJpsRcOJ43qQ_2ROnh9xNrxjl3wnPDehmTK9I68',
    'Connection': 'keep-alive',
    'Content-Length': '21',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': '_uab_collina=164993574180695922772105; Hm_lvt_f48055ef4cefec1b8213086004a7b78d=1649935743; auth={%22uid%22:%22WlhaaGVtaGhhUT09%22%2C%22uuid%22:%22WlhaaGVtaGhhUT09%22%2C%22refreshToken%22:%22eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJleHBpclwiOjE2NTUxMjgxMDA1MTQsXCJ1aWRcIjpcImV2YXpoYWlcIixcInV1aWRcIjpcIjEyMzQ1NlwifSIsImlhdCI6MTY0OTk0NDEwMH0.60X41vd9AbbnRdC1MgTAJS4r0bX-gNChMX4eeVjauGM%22%2C%22token%22:%22eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJleHBpclwiOjE2NTI1MzYxMDA1MTQsXCJ1aWRcIjpcImV2YXpoYWlcIixcInV1aWRcIjpcIjEyMzQ1NlwifSIsImlhdCI6MTY0OTk0NDEwMH0.5xpvKJpsRcOJ43qQ_2ROnh9xNrxjl3wnPDehmTK9I68%22}; winfanguser=uid=evazhai&nid=evazhai&logNum=14&err163=624343e3ebc754bb&pwd=f0a08fd2ebbfec1b7b4950f8db60c3&headerImg=http://user.winshang.com/images/pic/4.gif&sex=0&Email=zhaiyinlan_ait_yahoo.com.cn&IsCompany=0; eyeuser=uid%3devazhai%26nid%3devazhai%26logNum%3d14%26err163%3d624343e3ebc754bb%26pwd%3df0a08fd2ebbfec1b7b4950f8db60c3%26headerImg%3dhttp%3a%2f%2fuser.winshang.com%2fimages%2fpic%2f4.gif%26sex%3d0%26Email%3dzhaiyinlan_ait_yahoo.com.cn%26IsCompany%3d0; JSESSIONID=CC59A88B86ECA4CFB0A15592A4476148; Hm_lpvt_f48055ef4cefec1b8213086004a7b78d=1650937839',
    'Host': 'www.winshangdata.com',
    'Origin': 'https://www.winshangdata.com',
    'platform': 'pc',
    'pwd': pwd,
    'Referer': 'https://www.winshangdata.com/projectDetail?projectId=49406',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJleHBpclwiOjE2NTI1MzYxMDA1MTQsXCJ1aWRcIjpcImV2YXpoYWlcIixcInV1aWRcIjpcIjEyMzQ1NlwifSIsImlhdCI6MTY0OTk0NDEwMH0.5xpvKJpsRcOJ43qQ_2ROnh9xNrxjl3wnPDehmTK9I68',
    'uid': uid,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'uuid': '123456',
        
    }
    
    column_name = ['projectId', 'projectCityName', 'zhouBian.changZhuRenKou.value','zhouBian.changZhuRenKou.tongCheng', 
                    'zhouBian.banGongRenKou.value', 'zhouBian.banGongRenKou.tongCheng', 'zhouBian.chaiLvRenKou.value',
                    'zhouBian.chaiLvRenKou.tongCheng', 'zhouBian.gongJiaoZhan.value','zhouBian.gongJiaoZhan.tongCheng', 
                    'zhouBian.diTieZhan.value','zhouBian.diTieZhan.tongCheng', 'zhouBian.tingCheChang.value',
                    'zhouBian.tingCheChang.tongCheng', 'zhouBian.passengerFlow.value',
                    'zhouBian.passengerFlow.tongCheng', 'zhouBian.xiaoXue.value',
                    'zhouBian.xiaoXue.tongCheng', 'zhouBian.zhongXue.value',
                    'zhouBian.zhongXue.tongCheng', 'zhouBian.daXue.value',
                    'zhouBian.daXue.tongCheng', 'zhouBian.fangZu.value',
                    'zhouBian.fangZu.tongCheng', 'zhouBian.puZu.value',
                    'zhouBian.puZu.tongCheng', 'zhouBian.renJunMinaJi', 'chengShiGdp.nianFen.value', 
                    'chengShiGdp.value', 'chengShiXiaoFei.nianFen.value', 'chengShiXiaoFei.value']
    
    df = pd.DataFrame(columns=column_name)
    postUrl = 'https://www.winshangdata.com/wsapi/project/detailProjectFenXi'
    for id in id_list:
       
        # payloadData数据
        payloadData = {
         'projectId': id
        }
        

        dumpJsonData = json.dumps(payloadData)
        res = requests.post(postUrl, data=dumpJsonData, headers=payloadHeader )
        
        if res.status_code==200: 
            content = res.json()['data']
            df_temp2 = pd.json_normalize(content)
        else:
            ### fill with NA
            df_temp2 = pd.DataFrame([[id]+['N/A']*(len(column_name)-1) ])

        
        df = df.append(df_temp2,ignore_index = True)
        
    return df
