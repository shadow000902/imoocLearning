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

sql_insert = "insert into user(userid, username) VALUE (10, 'name10')"
sql_update = "update user set username='name91' WHERE userid=9"
sql_delete = "delete from user WHERE userd<3"

# 保证一组事务，要么都执行，要么都不执行
try:
	cursor.execute(sql_insert)
	print cursor.rowcount
	cursor.execute(sql_update)
	print cursor.rowcount
	cursor.execute(sql_delete)
	print cursor.rowcount

	conn.commit()
except Exception as e:
	print e
	# 捕捉到异常，回滚该组事务，不执行任何操作
	conn.rollback()

cursor.close()
conn.close()
