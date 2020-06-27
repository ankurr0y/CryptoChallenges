import codecs,base64
hex_number="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
b64=codecs.encode(codecs.decode(hex_number,"hex"),"base64").decode()
print(b64)
print(base64.b64decode(b64))
