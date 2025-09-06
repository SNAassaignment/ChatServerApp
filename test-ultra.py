# from threading import Thread
# from time import sleep

# a = []

# b = []


# def put():
#     sleep(1)
#     a.append(1)

# def putb():
#     sleep(1)
#     b.append(2)

# Thread(target=put,daemon=True).start()
# Thread(target=putb,daemon=True).start()

# def showall():
#     for c in a:
#         print(c)

# while True:
#     showall()
#     sleep(0.3)

from socket import *

s = socket(AF_INET,SOCK_DGRAM)
s.connect(('127.0.0.1',2222))
s.sendall('Usdfh'.encode())
s.close()