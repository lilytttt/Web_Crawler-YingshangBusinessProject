#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 20:21:44 2022

@author: ttlily
"""
import pandas as pd

from ZhoubianFenxi import zhoubian_fenxi
from project_list import project_list_collect
from project_detail import project_list_collection




# 添加自己的账号密码,如果不添加uid和pwd,返回结果是全是0
### 注意不是账号密码原文
### 参考  http://www.winshangdata.com/wsapi/project/detailProjectFenXi request header
uid = ''
pwd = ''


# 第一页项目列表 +  项目总数
result = project_list_collect(1)
if result[0] != 'error':
    total_projects_number = result[0]
    project_list_temp = result[1]
    
    id_list = project_list_temp['projectId'].tolist()
    print('Page 1 project list collected successfully.')
    # 第一页项目详情
    result_detail_temp = project_list_collection(id_list)
    print('Page 1 detail collected successfully.')

    # 第一页周边分析
    result_zhoubian_temp = zhoubian_fenxi(uid, pwd, id_list)
    print('Page 1 zhoubian collected successfully.')
    
    final_result = pd.concat([project_list_temp, result_detail_temp, result_zhoubian_temp], axis=1)
    
    
    total_page_number = int(total_projects_number/60)+1
    #total_page_number = 2
    # 2-最
    for i in range(2,(total_page_number+1)): 
        #### Step 1: 项目列表
        result = project_list_collect(i)
        if result[0] != 'error':
            project_list_temp = result[1]
            
            id_list = project_list_temp['projectId'].tolist()
            print('Page ', i, 'project list collected successfully.')
            # 第一页项目详情
            result_detail_temp = project_list_collection(id_list)
            print('Page ', i, ' detail collected successfully.')

            # 第一页周边分析
            result_zhoubian_temp = zhoubian_fenxi(uid, pwd, id_list)
            print('Page ', i, 'zhoubian collected successfully.')
            
            temp_df = pd.concat([project_list_temp, result_detail_temp, result_zhoubian_temp], axis=1)
            final_result =final_result.append(temp_df,ignore_index = True)
        else:
            print('Page ', i , 'project list failed. Continue with next page.')
    final_result.to_excel('result.xlsx')
    print('Finished!') 
    
else:
    print('Collecting page 1 failed. Total project failed')







