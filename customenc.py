from hashlib import sha256
key = 'mohamed'
def encrypt(value,key):
    return sha256(str(key+value).encode()).hexdigest()

def decrypt(value:str,key:str,enc_value:str) -> str:
    return value if sha256(str(key+value).encode()).hexdigest() == enc_value else None
    
value = 'Hi, this is my secret password'
enc = encrypt('Hi, this is my secret password',key)
dec = decrypt(value,key,enc)

print(f'Encrypted : {enc}\nDecryped : {dec}')