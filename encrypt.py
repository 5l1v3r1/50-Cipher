from hashlib import md5,sha256,sha512
import binascii,time
from machanizm import *
banner()

key=raw_input('['+y+'+'+rr+'] key : ')
message=raw_input('['+y+'+'+rr+'] Text : ')
def hash(key,message):
	g=''
	x=key
	for i in message:
		g=g+chr(table(x).find(i))
		x=x+i
	return g


start=time.time()
print binascii.hexlify(hash(key,message))
print time.time()-start

