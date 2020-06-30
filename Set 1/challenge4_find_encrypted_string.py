from binascii import unhexlify
from challenge3_xor_cipher import decypher

with open('lines.txt') as f:
    input_strings=[]
    for F in f:
        input_strings.append(unhexlify(F.strip()))

def isodd(string):
    if(len(string)%2==0):
        return False
    else:
        return True

candidates=[]
for i in range(ord('A'),ord('Z')):
    candidates.append(i)
for i in range(ord('a'),ord('z')):
    candidates.append(i)
candidates.append(ord(' '))
best=0
actual_message=[]
for input_string in input_strings:
    count=0
    message=decypher(input_string,candidates)
    '''actual_message=''
    for m in message:
        actual_message+=chr(m)'''
    for m in message:
        for c in candidates:
            if(m==c):
                count+=1
    if count>best:
        best=count
        actual_message=message
actual_message_translated=''
for a in actual_message:
    actual_message_translated+=chr(a)
print(actual_message_translated)#Now that the paarty is jumping

