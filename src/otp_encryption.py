import os
import string


class OTP:

    def __init__(self, input_data):
        self.key = self.gen_key(input_data)
        self.abc = '0123456789abcdef'

    def gen_key(self, msg) -> string:
        """
        The random module that comes with Python does not generate truly random numbers.
        They are computed from an algorithm that creates numbers that only appear random (which is often good enough).
        If the pad is not generated from a truly random source, then it loses its mathematically-perfect secrecy.
        The os.urandom() function can provide truly random numbers but is a bit more difficult to use.
        """
        msg_len = len(msg)
        print('msg_len: ', msg_len)
        return os.urandom(msg_len).hex()[:msg_len]

    def en_de_crypt(self, msg, en: bool = True) -> string:
        if en:
            cipher_msg = ''
            for ind, char in enumerate(msg):
                cipher = (self.abc.index(self.key[ind]) + self.abc.index(char)) % len(self.abc)
                cipher_msg += self.abc[cipher]
            return_msg = cipher_msg
        else:
            original_msg = ''
            for ind, char in enumerate(msg):
                plain = (self.abc.index(char) - self.abc.index(self.key[ind])) % len(self.abc)
                original_msg += self.abc[plain]
            return_msg = original_msg

        return return_msg


