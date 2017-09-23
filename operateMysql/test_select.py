# -*- coding: utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(
	host='127.0.0.1',
	port=3306,
	user='root',
	passwd='123456',
	db='imooc',
	charset='utf8'
)
cursor = conn.cursor()

sql = "select * from user"
cursor.execute(sql)

rs = cursor.fetchall()
for row in rs:
	print "userid=%s, username=%s" % row

cursor.close()
conn.close()
