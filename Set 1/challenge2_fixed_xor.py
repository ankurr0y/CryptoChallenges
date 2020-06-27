import codecs
def fixed_xor(xor_string):
    decoded_string=str(codecs.decode(xor_string,"hex"))
    print(decoded_string)
    fixed_string="686974207468652062756c6c277320657965"
    return(int(xor_string,base=16) ^ int(fixed_string,base=16))

xor_string="1c0111001f010100061a024b53535009181c"
result=fixed_xor(hex(int(xor_string)))
print(result)
#Not working yet
