from binascii import unhexlify
def bitwise_xor(a,b):
    return ([x^y for x,y in zip(a,b)])

string1=b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key=b'ICE'
keystream=key*(len(string1)//len(key)+1)
test_value=unhexlify(b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')
ciphertext=bitwise_xor(string1,keystream)
cipher_string=''
for c in ciphertext:
    cipher_string+=chr(c)
print(cipher_string)
print(test_value)
