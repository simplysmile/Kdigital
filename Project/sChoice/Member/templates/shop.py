from django.http import JsonResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd 
import json
import numpy as np
import matplotlib.pyplot as plt

# BEST100 csv파일 저장
filename="BEST_100.csv"
f=open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)
title = "제목 할인가격 리뷰 링크".split(" ")
writer.writerow(title)

# page별 best100 가져오기
for page in range(1,5):
    url="http://dshop.dietshin.com/goods/goods_best.asp?sort=BEST&gotopage={}".format(page)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")

    items = soup.find_all("li",{"class":"tb_mw_wrap"})
    # print(len(items))
    for i,item in enumerate(items):
        data=[]
        item_title = item.find("div",{"class":"best_n_box"}).span.get_text()
        # print('item_title : ',item_title)

        item_price =item.find("span",{"class":"best_n_list_dc"}).get_text()
        item_price = int(re.sub(r'[^0-9]','',item_price))
        # print('item_price : ',item_price)

        item_review =item.find("span",{"class":"b_n_reviw_num noto_sans mt5"}).get_text()
        item_review= int(re.sub(r'[^0-9]','',item_review))
        # print('item_review : ',item_review)

        all_a = item.find_all('a')
        # print(all_a)
        item_link =all_a[1]['href']
        item_link = "https://dshop.dietshin.com"+item_link
        # print('item_link : ',item_link)


        # print("*"*50)
        data.append(item_title)
        data.append(item_price)
        data.append(item_review)
        data.append(item_link)

        writer.writerow(data)
f.close()
################################################################################

import pandas as pd 
import json
import numpy as np
import matplotlib.pyplot as plt

def bestItems(request): 
    df = pd.read_csv("BEST_100.csv")
    # print(df)
    js_item={}
    js = df.to_json()
    js_item['json_data'] = json.loads(js)
    print(js_item['json_data'])
    context = {'js_item':js_item}
    return JsonResponse(context,safe=False)
