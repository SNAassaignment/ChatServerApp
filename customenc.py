# def encrypt(value):
#     getall = list()

#     for i in range(len(value)):
#         getall.append(str(i))
#         getall.append(value[i])

#     print(''.join(getall))

# def decrypt(value):
#     dec_val = ''
#     for i,rm in enumerate(list(value)):
#         if str(i) in rm:
#             pass
#         else:
#             dec_val += rm

#     print(dec_val[::2])

# encrypt('mohamed')
# decrypt('0m1o2h3a4m5e6d')

import base64

def encrypt(payload:str,key:str) -> bytes:
    final = (str(base64.b85encode(payload.encode())) + str(base64.a85encode(key.encode()))).encode()
    return base64.b64encode(final).decode().removesuffix('=').encode()

def decrypt(value:bytes,key:str) -> str:
    # will be continued...
    # print(decode)
    # print(key)
    pass


print(encrypt('mohamed','SECRET'))
print(decrypt(b'YidaRXQ4e1pEbksnYic7YWomTzc4cyc','SECRET'))