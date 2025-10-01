# # def encrypt(value):
# #     getall = list()

# #     for i in range(len(value)):
# #         getall.append(str(i))
# #         getall.append(value[i])

# #     print(''.join(getall))

# # def decrypt(value):
# #     dec_val = ''
# #     for i,rm in enumerate(list(value)):
# #         if str(i) in rm:
# #             pass
# #         else:
# #             dec_val += rm

# #     print(dec_val[::2])

# # encrypt('mohamed')
# # decrypt('0m1o2h3a4m5e6d')

# import base64

# def encrypt(payload:str,key:str) -> bytes:
#     enc_payload = base64.b16encode(payload.encode()).lower()
#     enc_key = base64.b16encode(key.encode()).lower()

#     final = enc_payload + b'}' + enc_key
#     return final

# def decrypt(value:bytes,key:str) -> str:
#     val = value.decode()
#     payload = val.split('}')[0]
#     print(base64.b16decode(payload.upper()))


# print(encrypt('mohamed','SECRET'))
# decrypt(b'6d6f68616d6564}534543524554','aaaaaaaa')
# # decrypt(b'YidaRXQ4e1pEbksnYic7YWomTzc4cyc','SECRET')
from base64 import b85encode,b85decode
def encrypt(payload:str):
    return b85encode(payload.encode())

def decrypt(value:bytes):
    return b85decode(value).decode()