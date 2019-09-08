from hashlib import md5,sha256,sha512
import binascii,time
d=''
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
rr = '\033[39m'
def spli(message):
	k=len(message)
	l=-2
	m=0
	end=[]
	while m<k:
		try:
			l=l+2
			m=m+2
			end.append(message[l:m])
		except:
			end.append(message[l:k])
			m=k+1
	return end
for i in range(255):
        d=d+chr(i)

def table(key):
	c=0
	b=''
	while len(b)<255 :
		for i in md5(key*c).digest():
			if i not in b:
				b=b+i
		for i in sha256(key*c).digest():
			if i not in b:
				b=b+i
		for i in sha512(key*c).digest():
			if i not in b:
				b=b+i
		c=c+1
	return b
	

def banner():
	r = '\033[31m'
	g = '\033[32m'
	y = '\033[33m'
	b = '\033[34m'
	m = '\033[35m'
	c = '\033[36m'
	w = '\033[37m'
	rr = '\033[39m'
	colors=[r,g,y,b,m,c,w,rr]
	import random
	pp='''
		           _.-=-._     .-,     '''+random.choice(colors)+'''SOMETHING IS A JOKE!
		         .'       "-.,' /        '''+random.choice(colors)+'''-\_(^_^)_/-
		        (  41-TRK   _.  <          
		         `=.____.="  `._\\  '''
	for i in pp.split('\n'):
		print random.choice(colors)+i
	print rr+'\n'
