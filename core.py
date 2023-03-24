import random


ALPHABET_ALL = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CASE = [str.upper, str.lower]


def to_num(s: str):
    return list(map(ord, s))

def convert_base(num, to_base=10, from_base=10, ALPHABET=None):
    # first convert to decimal number
    n = int(num, from_base) if isinstance(num, str) else num
    # now convert decimal to 'to_base' base
    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        #print(n, m, to_base)
        res += ALPHABET[m]
    return res[::-1] if res[::-1] else "0" 

def encode(text, key, BASE):
    ALPHABET = ALPHABET_ALL[:BASE]
    SALT = ALPHABET_ALL[BASE:]

    lt, lk = len(text), len(key)

    # нормируем ключ
    if lt <= lk:
        text = "_"*(lk - lt) + text
    else:
        key = key * (lt // lk) + key[:(lt % lk)]
    
    # переводим в желаемую систему счисления
    code_nums = list(map(lambda t: str(t[0]^t[1]) ,zip(to_num(key), to_num(text))))    
    code_nums_26 = [convert_base(x, to_base=BASE, from_base=10, ALPHABET=ALPHABET) for x in code_nums]

    #добавляем соль
    res = ""
    for num in code_nums_26:
        res += CASE[random.randint(0,1)](num)
        res += CASE[random.randint(0,1)](SALT[random.randint(0, len(SALT)-1)])

    return res, BASE

def decode(text, key, BASE):
    ALPHABET = ALPHABET_ALL[:BASE]
    SALT = ALPHABET_ALL[BASE:]

    # Избавляемся от соли, разбиваем по буквам (по их коду)
    text_filtered_splitted = "".join([c.replace(c, "_") if c.upper() in SALT else c.upper() for c in text]).strip("_").split("_")
    code_in_dec = [int(convert_base(num, to_base=10, from_base=BASE, ALPHABET=ALPHABET)) for num in text_filtered_splitted]

    #нормируем ключ
    lk, lt = len(key), len(code_in_dec)
    if lt > lk:
        key = key * (lt // lk) + key[:(lt % lk)]

    return "".join(list(map(lambda t: chr((t[0]^t[1]) % 0x110000), zip(list(code_in_dec), to_num(key))))).strip("_")
