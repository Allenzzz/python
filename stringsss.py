#encoding=utf-8

# print ('Price of egg is $%d' % 32)

# from math import pi
# print ('Pi:%f' % pi)

# print ('%+.2f' % 3983.7)+'\n'+('% 9.3f' % -910.1)
'''
	格式化打印字符串
'''
# width = input('Please enter width:')
# price_width = 10
# item_width = width-price_width

# header_format = '%-*s%*s'
# format = '%-*s%*.2f'

# print ('=' * width)
# print (header_format % (item_width,'Item',price_width,'Price'))
# print ('-' * width)
# print (format % (item_width,'Apples',price_width,0.5))
# print (format % (item_width,'Pears',price_width,0.4))
# print ('-' * width)

''' join '''

dirs='','usr','bin','env'

print ('/'.join(dirs))
print ('C:'+'\\'.join(dirs))