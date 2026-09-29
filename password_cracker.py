import zipfile 
import zlib 

def listofpasswords(filename):
    with open(filename, encoding='utf-8') as f:
        passwords = []
        for line in f:
            text = line.strip()
            passwords.append(text)
    return passwords

def testwhitehouse(zip_filename, passwords):
    with zipfile.ZipFile(zip_filename) as zf:
        count = 1
        for password in passwords:
            count += 1
            if count % 10000 == 0:
                print(count, password)
            try:
                zf.extractall(pwd=password.encode())
                print(password)
                return password
            except RuntimeError:
                continue
            except zipfile.BadZipFile:
                continue
            except zlib.error:
                continue

passwords_compiled = listofpasswords('Ashley-Madison.txt')
testwhitehouse('whitehouse_secrets.zip', passwords_compiled)