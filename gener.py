#-*-encoding:utf-8-*-
import mysql.connector
# def gg():
# aa,bb,cc=[],[],[]
# aa=[x+y+z for x in 'ABC' for y in 'omu' for z in 'bty']
# for i in range(len(aa)):
# 	cc.append(i)
# print bb

aa,bb=[],[]
aa=[x+y+z for x in 'ABC' for y in 'omu' for z in 'bty']
for i in range(len(aa)):
	t=('2015%04d' % i,aa[i])
	bb.append(t)
print len(bb)

db=mysql.connector.connect(user='allen',password='allen',database='test')
cur=db.cursor()

sql_insert=('INSTER INTO USER VALUES(%s,%s)')

for i in range(len[bb]):
	cur.execute(sql_insert,bb[i])
	cur.rowcount
	db.commit()
cur.close()
