from Crypto.Util.number import *
import binascii

cyph = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
b = long_to_bytes(cyph) #translate decimal representation to binary data

print(binascii.b2a_qp(b))
