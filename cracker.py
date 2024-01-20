import zipfile

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password.encode('utf-8'))
        print("Password found: " + password)
        return True
    except:
        return False

zip_filename = input("Enter file zip name : ")
wordlist_filename = input("Enter wordlist name : ")

try:
    zFile = zipfile.ZipFile(zip_filename)
except zipfile.BadZipFile:
    print("zip invalid")
    exit(1)

try:
    passFile = open(wordlist_filename, 'r')
except FileNotFoundError:
    print("wordlist not found")
    exit(1)

for line in passFile.readlines():
    password = line.strip("\n")
    found = extractFile(zFile, password)
    if found:
        exit(0)

print('Password not find')
