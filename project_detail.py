#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:20:36 2022

@author: ttlily
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup


def check_valid(result):
    if len(result) == 0:
        return False
    else:
        return True

def project_list_collection(id_list):
    column_name = ['projectId', 'projectName', 'projectDescrip', 
                'projectStatus', 'projectBusiness', 
                'type', 'opening_time', 
                'area',  'open_floor', 
                'city', 'address', 
                'isProductProject', 'intro', 
                'facility', 'developers']
    df = pd.DataFrame(columns=column_name)
    for id in id_list:
        url = 'http://www.winshangdata.com/projectDetail?projectId=' + str(id)
        response = requests.get(url)
        if response.status_code == 200: 
            soup = BeautifulSoup(response.text, "html.parser")
            #print(soup.prettify())  #輸出排版後的HTML內容
            temp_list = []
            temp_list.append(id)
            result = soup.find_all("h1", class_="detail-one-tit", limit=3)
            if check_valid(result):
                name = result[0].text
                name = name.replace('\n', '')
                name = name.replace(' ', '')
            else:
                name = ' '
            temp_list.append(name)
            
            result = soup.find_all("p", class_="detail-company", limit=3)
            if check_valid(result):
                descrip = result[0].text
                descrip = descrip.replace('\n', '')
                descrip = descrip.replace(' ', '')
            else:
                descrip = ' '
            
            temp_list.append(descrip)
            
            result = soup.find_all("div", class_="detail-three-tit", limit=3)
            if check_valid(result):
                status = result[0].text
                business_status = result[1].text
                
            else:
                status = ' '
                business_status = ' '
            temp_list.append(status)
            temp_list.append(business_status)
            
            result1 = soup.find_all("span", class_="detail-option-name")
            result2 = soup.find_all("span", class_="detail-option-value")
            
            
            for i in range(len(result1)):
                content = result1[i].text + result2[i].text 
                temp_list.append(content)
            
            
            result1 = soup.find_all("div", class_="detail-two-tit", limit=5)
            result2 = soup.find_all("div", class_="detail-richtext", limit=3)
            for i in range(len(result2)):
                content = result1[i+2].text + result2[i].text 
                #print(content)
                temp_list.append(content)
            
            df_temp1 = pd.DataFrame([temp_list], columns=column_name)
        else:
            df_temp1 = pd.DataFrame( [[id] + ['NA'] * (len(column_name)-1)])
        
        df = df.append(df_temp1,ignore_index = True)
            
    return df