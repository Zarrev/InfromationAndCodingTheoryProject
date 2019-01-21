import random
import string


class Channel:

    def __init__(self, msg, bit_error: float = 0.3):
        self.bit_error = bit_error
        self.msg = msg
        self.error_vector = self.cacl_error_vec()

    def cacl_error_vec(self):
        return ''.join(['1' if random.random() <= self.bit_error else '0' for _ in range(len(self.msg))])

    @staticmethod
    def xor_strs(str1: string, str2: string):
        if len(str1) != len(str2):
            raise Exception('The two string size is not matching!')

        return ''.join(['1' if str1[i] != str2[i] else '0' for i in range(len(str1))])

    def send_msg(self):
        return Channel.xor_strs(self.msg, self.error_vector)

    def set_msg(self, msg):
        self.msg = msg
        self.error_vector = self.cacl_error_vec()

    def set_bit_err(self, error):
        self.bit_error = error
        self.error_vector = self.cacl_error_vec()
