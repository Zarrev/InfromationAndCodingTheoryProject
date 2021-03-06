import os
import string


class OTP:
    """
    This class implements the one-time-pad encoder/decoder and key generator. The one-time pad (OTP) encryption
    technique is the only proven unbreakable encryption system. Even infinite computational power and time cannot break
    this system. It allows to use any language (English, Chinese, Russian etc). All texts are considered UTF-8 encoded.
    UTF-8 is a multi-byte encoding that can represent any Unicode character in 1 to 4 bytes. Each character in the
    message will be converted into a hexadecimal value. To encrypt the message It use a randomly generated number what
    we call a one-time pad.

    Note: I left the self.key class variable in the code because of the easier testing, but in general way it mustn't
    contains it.
    """
    abc = '0123456789abcdef'

    def __init__(self):
        self.key = None

    def load_key(self, key):
        """
        :param key: key in hexadecimal values
        """
        self.key = key

    def gen_key(self, msg) -> string:
        """
        The random module that comes with Python does not generate truly random numbers.
        They are computed from an algorithm that creates numbers that only appear random (which is often good enough).
        If the pad is not generated from a truly random source, then it loses its mathematically-perfect secrecy.
        The os.urandom() function can provide truly random numbers.
        :param msg: data what we want to encrypt. This data's coding is hexadecimal.
        """
        msg_len = len(msg)
        self.key = os.urandom(msg_len).hex()[:msg_len]

    def en_de_crypt(self, msg, en: bool = True) -> string:
        """
        This function implements the encryption and decryption.
        :param msg: data what we want to encrypt. This data's coding is hexadecimal.
        :param en: This parameter switch between the decryption and encryption. In the default state, the function will
                   encrypt the data.
        :return: The return value depends on the de- or encryption, but in every case it returns a string in hexadecimal
                 form.
        """
        if en:
            cipher_msg = ''
            for ind, char in enumerate(msg):
                cipher = (OTP.abc.index(self.key[ind]) + OTP.abc.index(char)) % len(OTP.abc)
                cipher_msg += OTP.abc[cipher]
            return_msg = cipher_msg
        else:
            original_msg = ''
            for ind, char in enumerate(msg):
                plain = (OTP.abc.index(char) - OTP.abc.index(self.key[ind])) % len(OTP.abc)
                original_msg += OTP.abc[plain]
            return_msg = original_msg

        return return_msg
