a = [
    {'name':'nammathan'},
    {'name':'Mazeeth'},
    {'name':'nammathan'},
    {'name':'nammathan'},
    {'name':'nammathan'},
    {'name':'nammathan'},
    {'name':'nammathan'},
    {'name':'nammathan'},
    {'name':'nammathan'},
    {'name':'nammathan'}
]

b = set()

for i in a:
    b.add(i['name'])

print(b)