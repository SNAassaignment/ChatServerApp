# import os
# import time
# from datetime import datetime

# # Path to your screenshots folder
# screenshot_dir = '/home/mohamed/Pictures/Screenshots'

# # Initially known screenshots
# known_files = set(os.listdir(screenshot_dir))

# print("[*] Monitoring for new screenshots...")

# while True:
#     time.sleep(0.2)  # Check every second
#     current_files = set(os.listdir(screenshot_dir))
#     new_files = current_files - known_files

#     if new_files:
#         for f in new_files:
#             if f.endswith(".png"):
#                 now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 print(f"[✔] Screenshot detected: {f} at {now}")
#         known_files = current_files

a = {'a','c','q'}
b = {'a','c','q','o'}
print(a)
print(b)
c = b - a
print(c)
