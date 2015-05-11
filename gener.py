#-*-coding:utf-8-*-
import mysql.connector as mconn
# def gg():
# aa,bb,cc=[],[],[]
# aa=[x+y+z for x in 'ABC' for y in 'omu' for z in 'bty']
# for i in range(len(aa)):
# 	cc.append(i)
# print bb

aa,bb=[],[]
aa=[x+y+z for x in 'ABC' for y in 'omu' for z in 'bty']
for i in range(len(aa)):
	t=('2015%04d' %(i+1),aa[i])
	bb.append(t)
# print len(bb)
try:
	db=mconn.connect(user='allen',password='allen',database='test')
	cur=db.cursor()

	sql_insert=('INSTER INTO USER VALUES(%s,%s)')

	for i in range(len(aa)):
		cur.execute(sql_insert,bb[i])
		cur.rowcount
	db.commit()
except mconn.Error, e:
	raise e('dkddddd')
	# print ('Error:%s'%e.args[0])
finally:
	if db:
		cur.close()


