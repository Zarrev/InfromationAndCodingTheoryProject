class Transmitter:

    def __init__(self, msg, repeat_num):
        self.msg = msg
        self.repeat_num = repeat_num
        self.coded_msg = Transmitter.coding_msg(self.msg, self.repeat_num)

    @staticmethod
    def coding_msg(msg, repeat_num):
        coded_msg_array = [str(x) * repeat_num for x in msg]
        return ''.join(coded_msg_array)
