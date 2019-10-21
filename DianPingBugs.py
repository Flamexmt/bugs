import time

import get_all_comments

headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.46',
        'Cookie': '_lxsdk_cuid=16dde991908c8-0b860b4d836be3-b363e65-1fa400-16dde991909c8; _lxsdk=16dde991908c8-0b860b4d836be3-b363e65-1fa400-16dde991909c8; _hc.v=d8cbb341-a33d-32e7-5683-3e9593c9c037.1571397639; ua=%E6%9D%82%E7%B2%AE%E9%A6%92%E5%A4%B4%E3%80%81; ctu=989b3613b00cf7238c76678757bcfa75d26b84d4a31fe61bc897babc96b593ab; s_ViewType=10; cy=5; cye=nanjing; dper=a341726fa1431b657ae8d2ff293657a44d251d5d358fc204aa22b79dc69e310fc00186fb2d78058ed15d052c0287b46c85b869f27706c4c2f477676bd2f6fa9766a4d2a334a275c98bf4d1268618a33b82be03de7a4c5fdb6805d0f0b66fde19; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; ll=7fd06e815b796be3df069dec7836c3df; _lxsdk_s=16dedbd61d3-e45-cc6-13%7C%7C507',
    }
shop_list=[]
with open('all_shops.txt',encoding='UTF-8') as f:
    for line in f:
        shop_list.append(line)
f.close()

for line in shop_list:
    shop_id = line.split(' ')[0]
    get_all_comments.get_comments_ids(shop_name=line.split(' ')[1][:-2], shop_id=shop_id, headers=headers)
    time.sleep(3)