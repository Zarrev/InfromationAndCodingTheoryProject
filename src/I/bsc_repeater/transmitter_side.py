class Transmitter:

    def __init__(self, msg, repeat_num):
        self.msg = msg
        self.repeat_num = repeat_num
        self.coded_msg = Transmitter.coding_msg(self.msg, self.repeat_num)

    @staticmethod
    def coding_msg(msg, repeat_num):
        coded_msg_array = [str(x) * repeat_num for x in msg]
        return ''.join(coded_msg_array)

    def get_coded_msg(self):
        return self.coded_msg

    def get_msg(self):
        return self.msg

    def get_repeat_num(self):
        return self.repeat_num

    # def recalc_coded_msg(self):
    #     self.coded_msg = Transmitter.coding_msg(self.msg, self.repeat_num)

    def set_msg(self, msg):
        self.msg = msg
        self.coded_msg = Transmitter.coding_msg(self.msg, self.repeat_num)

    def set_repeat_num(self, repeat_num):
        self.repeat_num = repeat_num
        self.coded_msg = Transmitter.coding_msg(self.msg, self.repeat_num)
