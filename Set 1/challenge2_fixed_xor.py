import codecs
def xor(b1,b2):
    b=bytearray(len(b1))
    for i in range(0,len(b1)):
        b[i]=b1[i] ^ b2[i]
    return b
input_string=bytearray.fromhex('1c0111001f010100061a024b53535009181c')
against_string=bytearray.fromhex('686974207468652062756c6c277320657965')
b=bytes(xor(input_string,against_string))
print(codecs.encode(b,"hex"))
print(b)
