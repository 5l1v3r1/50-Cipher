from hashlib import md5,sha256,sha512
import binascii,time
from machanizm import *

banner()
key=raw_input('key : ')
message=raw_input('message : ')
def dihash(key,message):
        g=''
        x=key
        for i in message:
                r=table(x)[d.find(i)]
                g=g+r
                x=x+g[message.find(i)]
        return g
start=time.time()
print dihash(key,binascii.unhexlify(message))
print time.time()-start
