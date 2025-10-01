from base64 import b85encode,b85decode
def encrypt(payload:str):
    return b85encode(payload.encode())

def decrypt(value:bytes):
    return b85decode(value).decode()