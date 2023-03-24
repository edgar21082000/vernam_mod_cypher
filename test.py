from random import randint
from core import encode, decode

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ _абвгдежзиклмнопрстуфхцчшщьыъэюя"
CASE = [str.upper, str.lower]

for i in range(1000):
    text = "".join([CASE[randint(0,1)](ALPHABET[randint(0,68)]) for _ in range(randint(10,30))])
    key = "".join([CASE[randint(0,1)](ALPHABET[randint(0,68)]) for _ in range(randint(10,30))])
    print(text)
    print(key)
    print("\n")


    enc = encode(text, key)
    dec = decode(enc, key)

    if text != dec:
        print("===========False==========")
        print(text)
        print(key)



