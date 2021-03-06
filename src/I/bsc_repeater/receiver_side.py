class Receiver:

    def __init__(self, received_msg, repeat_num):
        self.received = received_msg
        self.repeat_num = repeat_num
        self.decoded = self.decode()

    def decode(self):
        decoded = ''
        for i in range(len(self.received)//self.repeat_num):
            begin = i*self.repeat_num
            end = begin + self.repeat_num
            if self.received[begin:end].count('0') < self.received[begin:end].count('1'):
                decoded += '1'
            else:
                decoded += '0'

        return decoded

    def get_decoded(self):
        return self.decoded
