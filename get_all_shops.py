import re
import requests
import json

def get_all_shop_in_one_page(url='http://www.dianping.com/nanjing/ch10/o3',headers={}):
    print('come to here!!!')
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Cookie': 'navCtgScroll=0; navCtgScroll=0; _lxsdk_cuid=16dde991908c8-0b860b4d836be3-b363e65-1fa400-16dde991909c8; _lxsdk=16dde991908c8-0b860b4d836be3-b363e65-1fa400-16dde991909c8; _hc.v=d8cbb341-a33d-32e7-5683-3e9593c9c037.1571397639; dper=a341726fa1431b657ae8d2ff293657a4f558acfaacb9d7eab0f9e4b2e75b1f285f8a26ac990631c2bc5b8b5e5189c0a61cb528540a863be75228d7e3e7bb93546acef8e7e02dfa3cacb72c65a5bab892045cd769a2540f7aaaae59fdf7bc8aaf; ua=%E6%9D%82%E7%B2%AE%E9%A6%92%E5%A4%B4%E3%80%81; ctu=989b3613b00cf7238c76678757bcfa75d26b84d4a31fe61bc897babc96b593ab; s_ViewType=10; ll=7fd06e815b796be3df069dec7836c3df; cy=5; cye=nanjing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16de37f8d91-295-ad2-373%7C%7C992'
    }
    response = requests.get(url, headers=headers)
    shop_list_content=response.text
    pattern_str = 'ame="shop_title_click" data-shopid="(.*?)" data-hippo-type="shop"'
    pattern = re.compile(pattern_str, re.S)
    shop_id=re.findall(pattern,shop_list_content)
    pattern_str = ' data-hippo-type="shop" title="(.*?)"'
    pattern = re.compile(pattern_str, re.S)
    shop_name=re.findall(pattern,shop_list_content)
    print(shop_id)
    print(shop_name)
    with open('all_shops123123123.txt','a',encoding='utf-8') as f:
        for i in range(len(shop_id)):
            word=shop_id[i]+' '+shop_name[i]
            f.write(word)
            f.write('\n')

    return

