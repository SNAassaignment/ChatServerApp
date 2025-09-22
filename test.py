# # a = [
# #     {'name':'nammathan'},
# #     {'name':'Mazeeth'},
# #     {'name':'nammathan'},
# #     {'name':'nammathan'},
# #     {'name':'nammathan'},
# #     {'name':'nammathan'},
# #     {'name':'nammathan'},
# #     {'name':'nammathan'},
# #     {'name':'nammathan'},
# #     {'name':'nammathan'}
# # ]

# b = set({1,2,3,4,5,6,7,78,8})

# # for i in a:
# #     b.add(i['name'])

# # print(b)

# # a = ['mohamed','hunter']

# # for s in a:
# #     if s == 'maohamed':
# #         print(s)


# for i in b:
#     print(i)

import time

start = int(time.time() * 1000)
time.sleep(1)
end = int(time.time() * 1000)
print(f'start:{start}\nend:{end}')
print(f"Elapsed: {int((end - start) / 1000)} s") 