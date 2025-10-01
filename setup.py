from json import load,dump

print('\nTo setup your credentils:\n')
admin_username = input('Enter admin username : ')
admin_password = input('Enter admin password : ')

with open('credentials.json','r') as credfile:
    creds = load(credfile)
    creds['ADMIN_USERNAME'] = admin_username
    creds['ADMIN_PASSWORD'] = admin_password
    credfile.close()

with open('credentials.json','w') as credfilew:
    dump(creds,credfilew,indent=4)