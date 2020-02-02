import re
import time
import requests
import random_headers
import os
#coding=utf-8

def get_detail(root,file,detailfile):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Cookie':'shoppingCartSessionId=d9a4aa726ccbd48d1b62c6a4cfe0f6a1; reciever_area=1006000000; acw_tc=2760778a15802940251435596e597c20d4b69573e81d83048ab9383f70eec3; utm_source=101002001000; kfz_uuid=d428ded5-32d9-4120-9ef5-aee7092c58d7; kfz-tid=61c0ae12d270460a4983bce0b2f0d1e0; PHPSESSID=91ai6945q0nl63qdbl6mjfc101; Hm_lvt_33be6c04e0febc7531a1315c9594b136=1580294041,1580356702,1580360617; Hm_lvt_bca7840de7b518b3c5e6c6d73ca2662c=1580294041,1580356702,1580360617; kfz_trace=d428ded5-32d9-4120-9ef5-aee7092c58d7|0|42794677bbec2a4c|101002001000; TY_SESSION_ID=9e214bcf-96fd-4128-9f5c-6d845285ef12; Hm_lpvt_33be6c04e0febc7531a1315c9594b136=1580360646; Hm_lpvt_bca7840de7b518b3c5e6c6d73ca2662c=1580360646'
    }

    categoryfile=open(os.path.join(root,file),'r',encoding='utf-8')

    detailfile.write('\n')
    detailfile.flush()
    for line in categoryfile:
        url=line[:-1]
        print(url)
        response=requests.get(url,headers=headers)
        html_content=response.text
        html_content=html_content.replace('javascript:;','')
        pattern_str = '<h1 class="detail-title" itemprop="name">(.*?)</h1>.*? .*?'
        pattern = re.compile(pattern_str, re.S)
        detail = re.findall(pattern, html_content)
        if len(detail) > 0:
            detailfile.write(detail[0])
        else:
            detailfile.write('None')
        detailfile.write(',')
        detailfile.flush()

        if 'target="_blank"><img itemprop="image' in html_content:
            pattern_str = 'target="_blank"><img itemprop="image" id="mainInmg" src="(.*?)"'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                print(detail)
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        if '<a rel="nofollow"' in html_content:
            pattern_str = '<a rel="nofollow" href="(.*?)"'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
        if '<a itemprop="author"' in html_content:
            pattern_str = '<a itemprop="author".*?target="_blank">(.*?)</a>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()

        if '出版社' in html_content:
            pattern_str = '出版社:.*?<span class="text-value gray3">(.*?)</span>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        if '出版时间' in html_content:
            pattern_str = '出版时间:.*?<span class="text-value gray3">(.*?)</span>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        if 'ISBN' in html_content:
            pattern_str = 'ISBN:.*?<span class="text-value gray3">(.*?)</span>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        if '定价' in html_content:
            pattern_str = '定价:.*?<span class="text-value gray3">(.*?)</span>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        if '装帧' in html_content:
            pattern_str = '装帧:.*?<span class="text-value gray3">(.*?)</span>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        if '开本' in html_content:
            pattern_str = '开本:.*?<span class="text-value gray3">(.*?)</span>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()

        if '纸张' in html_content:
            pattern_str = '纸张:.*?<span class="text-value gray3">(.*?)</span>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()

        if '页数' in html_content:
            pattern_str = '页数:.*?<span class="text-value gray3">(.*?)</span>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()

        if '字数' in html_content:
            pattern_str = '字数:.*?<span class="text-value gray3">(.*?)</span>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()

        if '正文语种' in html_content:
            pattern_str = '正文语种:.*?<span class="text-value gray3">(.*?)</span>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()

        if '分类' in html_content:
            pattern_str = '分类:.*?<span class="text-value">(.*?)</span>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                detailfile.write(detail[0])
            else:
                detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write(',')
            detailfile.flush()

        if 'reviewBody' in html_content:
            pattern_str = '<h5 itemprop="reviewBody">内容简介: </h5>(.*?)</li>'
            pattern = re.compile(pattern_str, re.S)
            detail = re.findall(pattern, html_content)
            if len(detail)>0:
                result = detail[0].replace(' ','')
                result = result.replace('\n','')
                result = result.replace('&nbsp;', '')
                result = result.replace('<br/>', '')
                result = result.replace('<br>', '')
                result = result.replace('\n', '')
                detailfile.write(result)
            else:
                detailfile.write('None')
            detailfile.write('\n')
            detailfile.flush()
        else:
            detailfile.write('None')
            detailfile.write('\n')
            detailfile.flush()

        time.sleep(0.5)


for root, dirs, files in os.walk('D:/study/project/bugs/bookBug/books/item'):
    for item in files:
        filename = os.path.join(root, 'detail')
        filename = os.path.join(filename, item)
        detailfile = open(filename, 'a', encoding='utf-8')
        detailfile.write('书名,图片链接,豆瓣链接,作者,出版社,出版时间,ISBN,定价,装帧,开本,纸张,页数,字数,正文语种,分类,简介')
        detailfile.flush()
        print(root,item)
        get_detail(root,item,detailfile)
        time.sleep(1)