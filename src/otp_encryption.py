import os
import string
from base64 import b64encode


def gen_key(msg_len: int, decode: string = 'utf-8') -> string:
    """
    The random module that comes with Python does not generate truly random numbers.
    They are computed from an algorithm that creates numbers that only appear random (which is often good enough).
    If the pad is not generated from a truly random source, then it loses its mathematically-perfect secrecy.
    The os.urandom() function can provide truly random numbers but is a bit more difficult to use.
    """
    return b64encode(os.urandom(msg_len)).decode(decode)


def en_de_crypt(msg: string, key: string, en: bool = True) -> string:
    abc = string.printable + "öüóőúéáűíÖÜÓŐÚÉÁŰÍ"
    if en:
        cipher_msg = ''
        for ind, char in enumerate(msg):
            cipher = (abc.index(key[ind]) + abc.index(char)) % len(abc)
            cipher_msg += abc[cipher]
        return_msg = cipher_msg
    else:
        original_msg = ''
        for ind, char in enumerate(msg):
            plain = (abc.index(char) - abc.index(key[ind])) % len(abc)
            original_msg += abc[plain]
        return_msg = original_msg

    return return_msg
