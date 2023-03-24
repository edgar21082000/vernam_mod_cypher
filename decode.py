import getpass
from core import decode

    
text = input()
key = getpass.getpass()

print(decode(text, key))
