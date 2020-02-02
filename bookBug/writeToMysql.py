import pymysql

conn = pymysql.connect(
    host='172.19.240.141',
    port=3306,
    user='newuser', password='123456',
    database='project')
cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
sql = 'insert into product(pid,name,image,writer,press,time,ISBN,page,category,intro) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
import os
id=0
for root, dirs, files in os.walk('D:/study/project/bugs/bookBug/books/item/detail'):
    for item in files:
        filepath = os.path.join(root, item)
        detailfile = open(filepath, 'r', encoding='utf-8')
        for l in detailfile:
            pid = str(id).rjust(7, '0')
            details=l.replace('javascript:;','')[:-1].split(',')

            if(len(details)>=14) and '豆瓣链接' not in l:
                name = details[0]
                image = details[1]
                writer = details[2]
                press = details[3]
                time = details[4]
                ISBN = details[5]
                page = details[10]
                category = details[-2]
                intro = details[-1]
                id += 1
                print(pid, name, image, writer, press, time, ISBN, page, category, intro)
                cursor.execute(sql, [pid, name, image, writer, press, time, ISBN, page, category, intro])
                conn.commit()
cursor.close()
conn.close()
