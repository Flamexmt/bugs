import re
import time
import requests
import random_headers

#coding=utf-8
def get_comments_ids():
    indextext=open('index.txt','r',encoding='utf-8')
    indextxt=indextext.read()
    import sys
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Cookie':'shoppingCartSessionId=d9a4aa726ccbd48d1b62c6a4cfe0f6a1; reciever_area=1006000000; acw_tc=2760778a15802940251435596e597c20d4b69573e81d83048ab9383f70eec3; utm_source=101002001000; kfz_uuid=d428ded5-32d9-4120-9ef5-aee7092c58d7; kfz-tid=61c0ae12d270460a4983bce0b2f0d1e0; PHPSESSID=91ai6945q0nl63qdbl6mjfc101; Hm_lvt_33be6c04e0febc7531a1315c9594b136=1580294041,1580356702,1580360617; Hm_lvt_bca7840de7b518b3c5e6c6d73ca2662c=1580294041,1580356702,1580360617; kfz_trace=d428ded5-32d9-4120-9ef5-aee7092c58d7|0|42794677bbec2a4c|101002001000; TY_SESSION_ID=9e214bcf-96fd-4128-9f5c-6d845285ef12; Hm_lpvt_33be6c04e0febc7531a1315c9594b136=1580360646; Hm_lpvt_bca7840de7b518b3c5e6c6d73ca2662c=1580360646'
    }
    # print(url)
    # response=requests.get(url,headers=headers)
    # html_content=response.text
    # print(html_content)
    with open('smallcategory.txt','w',encoding='utf-8') as f:



#       pattern_str = 'href="\\/\\/www.dianping.com\\/review\\/(.*?)"'
#       pattern_str='<a class="detail-item-title-link" href="(http:\\/\\/item.kongfz.com\\/.*?\\/)" target="_blank">(.*?)<\\/a>'


        pattern_str = '<a class="detail-item-title-link"(.*?)<\\/a>'

        pattern = re.compile(pattern_str, re.S)
        bigcategory = re.findall(pattern, indextxt)
        print(len(bigcategory))
        for item in bigcategory:
            result=item.split('" target="_blank">')
            print(result[0][7:],result[1])
            f.write(result[0][7:])
            f.write(' ')
            f.write(result[1])
            f.write('\n')
def get_books(url,category):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Cookie':'shoppingCartSessionId=d9a4aa726ccbd48d1b62c6a4cfe0f6a1; reciever_area=1006000000; acw_tc=2760778a15802940251435596e597c20d4b69573e81d83048ab9383f70eec3; utm_source=101002001000; kfz_uuid=d428ded5-32d9-4120-9ef5-aee7092c58d7; kfz-tid=61c0ae12d270460a4983bce0b2f0d1e0; PHPSESSID=91ai6945q0nl63qdbl6mjfc101; Hm_lvt_33be6c04e0febc7531a1315c9594b136=1580294041,1580356702,1580360617; Hm_lvt_bca7840de7b518b3c5e6c6d73ca2662c=1580294041,1580356702,1580360617; kfz_trace=d428ded5-32d9-4120-9ef5-aee7092c58d7|0|42794677bbec2a4c|101002001000; TY_SESSION_ID=9e214bcf-96fd-4128-9f5c-6d845285ef12; Hm_lpvt_33be6c04e0febc7531a1315c9594b136=1580360646; Hm_lpvt_bca7840de7b518b3c5e6c6d73ca2662c=1580360646'
    }
    filename='books/'+category+'.txt'
    categoryfile=open(filename,'a',encoding='utf-8')
    response=requests.get(url,headers=headers)
    html_content=response.text
    if 'item' in url:
        pattern_str = '<a target="_blank" href="(.*?)" class="link">.*?</a>'
        pattern = re.compile(pattern_str, re.S)
        book = re.findall(pattern, html_content)
        print(len(book))
        for item in book:
            print(item)
            categoryfile.write(item)
            categoryfile.write('\n')
            categoryfile.flush()
    else:
        pattern_str = '<div class="btns-group clearfix"(.*?)</div>'
        pattern = re.compile(pattern_str, re.S)
        book = re.findall(pattern, html_content)
        for item in book:
            buyid=item.split('\n')[1].strip().split('\"')[1]
            shopid=item.split('\n')[2].strip().split('\"')[1]
            itemid=item.split('\n')[3].strip().split('\"')[1]
            print(buyid,shopid,itemid)

            categoryfile.write(buyid)
            categoryfile.write(' ')
            categoryfile.write(itemid)
            categoryfile.write(' ')
            categoryfile.write(itemid)
            categoryfile.write(' ')
            categoryfile.write('\n')
            categoryfile.flush()

with open('bigcategory.txt','r',encoding='utf-8') as f:
    for item in f:
        time.sleep(1)
        url=item.split(' ')[0]
        name=item.split(' ')[1][:-1]
        for page in range(10):
            time.sleep(1)
            if page==0:
                temp=url
            else:
                temp=url+'w'+str(page+1)+'/'
            print(temp)
            import  time
            get_books(temp,name)
