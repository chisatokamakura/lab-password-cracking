from zipfile import ZipFile
with open("Ashley-Madison.txt") as f:
    passwords = [line.strip() for line in f]

for i, password in enumerate(passwords):
    if i % 10000 == 0: 
        print(i, password)
    
    try: 
        with ZipFile("whitehouse_secrets.zip") as zf:
            zf.extractall(pwd=password.encode())

            print("Password:", password)
            break

    except: 
        continue
    





