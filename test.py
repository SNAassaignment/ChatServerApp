from datetime import datetime
from zoneinfo import ZoneInfo
from time import sleep
from os import system

while True:
    current_time = str(datetime.now(ZoneInfo('Asia/Kolkata'))).split(' ')[1].split('.')[0]
    print(current_time)
    sleep(0.1)
    system('clear')