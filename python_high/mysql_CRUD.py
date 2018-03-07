# -*- coding: utf-8 -*-
# @Time     :2018/3/2 下午2:22
# @Author   :李二狗
# @Site     :
# @File     :mysql_CRUD.py
# @Software :PyCharm

#   python 操作 mysql 数据库的三种方式： 1、 pymysql  2、 mysqldb  3、 sqlalchemy



#   pymysql

import pymysql

#   1 数据库的链接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='python_db', charset='utf8')
print(conn)

#   2 创建操作游标
cursor = conn.cursor()


#   3 设置字符的编码以及自动提交

# 字符编码
cursor.execute('set names utf8')
# 自动提交
cursor.execute('set autocommit=1')
# conn.commit()

#   4 编写sql语句
sql = "insert into tb_user(name, pwd) values('lichan123', '123456')"
delsql = "delete from tb_user where id=2"
delsql2 = 'delete from tb_user where id={0}'.format(3)

update = "update tb_user set pwd = 'ergou' where name = 'lichan'"

search = 'select * from tb_user'


#   5 执行sql 并得到结果集
#cursor.execute(sql)
cursor.execute(search)

#   得到结果集 fetchone() fetchmany(N) fetchall()
result = cursor.fetchmany(2)
print(result)

#   6 关闭游标和链接
cursor.close()
conn.close()