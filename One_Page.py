import re
import requests
import json


def get_one_page(url,headers=''):


    response=requests.get(url,headers=headers)
    if response.status_code == 200:
        review_text=response.text
        css_content=get_css_content(review_text,headers)
        review_words=get_review_word(review_text)
        css_words=get_css_word(review_words)

        word_dict={
            'ndy':'',
            'rhi':'',
            'cuq':'',
            'dvw':''
        }
        # 找到这个密码对应的那个svg图,一共有四类，ndy,rhi,cuq,dvw，暂时只需要ndy
        ndy_word_book=''
        pattern_str = 'class\\^="ndy".*?url(.*?);'
        pattern = re.compile(pattern_str, re.S)
        ndy_word_book = re.findall(pattern, css_content)[0]
        ndy_word_book=ndy_word_book[3:-1]
        ndy_word_book='http://'+ndy_word_book
        response = requests.get(ndy_word_book, headers=headers)
        ndy_word_book=response.text
        real_word=get_real_word_ndy(css_words[0],ndy_word_book,css_content)
        real_review=review_words
        for word in css_words:
            pattern_str = '<svgmtsi class="'+word+'"></svgmtsi>'
            pattern = re.compile(pattern_str, re.S)
            real_word=get_real_word_ndy(word,ndy_word_book,css_content)
            real_review=re.sub(pattern,real_word,real_review)
        real_review=clean_reviw(real_review)
        print(real_review)
        return real_review
    else:
        print('被封锁了')
    return None

def get_css_content(review_text,headers):
    pattern_str = '<link rel="stylesheet" type="text/css" href="//(s3plus.*?)">'
    pattern = re.compile(pattern_str, re.S)
    css_html = re.findall(pattern, review_text)[0]
    head = 'http://'
    css_html = head + css_html
    css_response = requests.get(css_html, headers=headers)
    return css_response.text


def get_review_word(review_text):
    pattern_str = '<div class="review-words">(.*?)</div>'
    pattern = re.compile(pattern_str, re.S)
    review_word = re.findall(pattern, review_text)[0]
    return review_word


def get_css_word(review_words):
    pattern_str = '<svgmtsi class="(.*?)"></svgmtsi>'
    pattern = re.compile(pattern_str, re.S)
    css_words = re.findall(pattern, review_words)
    return css_words

def get_real_word_ndy(css_word,word_book,css_content):
    pattern_str='.'+css_word+'{background:-(.*?).0px -(.*?).0px;}'
    pattern = re.compile(pattern_str, re.S)
    result=re.findall(pattern, css_content)
    position_x=result[0][0]
    position_y = result[0][1]
    position_x=abs(int(position_x))
    position_y=abs(int(position_y))
    position_x=int(position_x/14)
    big_small=[]
    #找到这个密码对应的那个svg图,暂时评论只需要ndy类的就行了
    pattern_str='d="M0(.*?)H'
    pattern = re.compile(pattern_str, re.S)
    for item in re.findall(pattern,word_book):
        big_small.append(int(item[1:-1]))
    for i in range(len(big_small)-1):
        if position_y<big_small[i]:
            position_y=1
            break
        if position_y>big_small[i] and position_y<big_small[i+1]:
            position_y=i+2
            break
    pattern_str='<textPath xlink:href="#'+str(position_y)+'" textLength=".*?">(.*?)</textPath>'
    pattern = re.compile(pattern_str, re.S)
    realword=re.findall(pattern,word_book)[0][position_x]
    return realword

def clean_reviw(real_review):
    pattern_str = '&#.*?;'
    pattern = re.compile(pattern_str, re.S)
    real_review = re.sub(pattern, '', real_review)
    pattern_str = '<img class.*?>'
    pattern = re.compile(pattern_str, re.S)
    real_review = re.sub(pattern, '', real_review)
    return real_review

# get_one_page('http://www.dianping.com/review/629367096')