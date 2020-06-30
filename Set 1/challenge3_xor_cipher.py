from binascii import unhexlify

def bitwise_xor(a,b):
    return ([x^y for (x,y) in zip(a,b)])

def decypher(input_string,candidates):
    best=None
    return_message=''
    for i in range(2**8):
        candidate_key=i.to_bytes(1,byteorder='big')
        keystream=candidate_key*len(input_string)
        message=bitwise_xor(input_string,keystream)
        count=0
        for m in message:
            for c in candidates:
                if (m==c):
                    count+=1
        if(best==None or best<count):
            best=count
            return_message=message
    return(return_message)

input_string=unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
candidates=[]
for i in range(ord('A'),ord('Z')):
    candidates.append(i)
for i in range(ord('a'),ord('z')):
    candidates.append(i)
candidates.append(ord(' '))
message_list=decypher(input_string,candidates)
message=''
print(message_list)
for m in message_list:
    message+=(chr(m))

print("Message is:"+str(message))
