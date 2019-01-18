import os
import string


def gen_key(msg_len: int, decode: string = 'latin1') -> string:
    """
    The random module that comes with Python does not generate truly random numbers.
    They are computed from an algorithm that creates numbers that only appear random (which is often good enough).
    If the pad is not generated from a truly random source, then it loses its mathematically-perfect secrecy.
    The os.urandom() function can provide truly random numbers but is a bit more difficult to use.
    """
    return os.urandom(msg_len).decode(decode)


def en_de_crypt(msg: string, key: string, en: bool = True) -> string:
    abc = string.ascii_lowercase
    list_of_abc = list(abc)
    if en:
        cipher_msg = ''
        for ind, char in enumerate(msg):
            cipher = (list_of_abc.index(key[ind]) + abc.index(char)) % len(abc)
            cipher_msg += abc[cipher]
        return_msg = cipher_msg
    else:
        original_msg = ''
        for ind, char in enumerate(msg):
            plain = (abc.index(char) - list_of_abc.index(key[ind])) % len(abc)
            original_msg += abc[plain]
        return_msg = original_msg

    return return_msg


if "__main__" == __name__:
    msg = "apa"
    key = gen_key(len(msg))
    ctext = en_de_crypt(msg, key)
    print(ctext)
    print(en_de_crypt(ctext, key, False))
