from base64 import b16decode, b64encode

data_hex=b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
data_raw=b16decode(data_hex,casefold=True)
data_b64=b64encode(data_raw)

print(f"{data_hex=}")
print(f"{data_raw=}")
print(f"{data_b64=}")




# import base64

# HEX_STRING = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# BYTE_ARRAY = bytearray.fromhex(HEX_STRING)
# print(BYTE_ARRAY)
# BASE64_VAL = base64.b64encode(BYTE_ARRAY)
# print(BASE64_VAL)


# string="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
# text=bytes.fromhex(string)
# print(text) #imprimindo a frase com bytes
