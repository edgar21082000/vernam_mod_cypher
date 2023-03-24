import getpass
from core import encode

    
text = input()
key = getpass.getpass()

print(encode(text, key))
    
    



