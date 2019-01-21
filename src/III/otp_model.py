from III import origin_model as om, otp_encryption as oe


class OTP_M(om.Model):

    def __init__(self):
        super().__init__()
        self.otp = oe.OTP()

    def set_input(self, _input):
        self.input = _input
        print(self.input)

    def set_key(self, key=None):
        if key is not None:
            self.otp.load_key(key)
        else:
            self.otp.gen_key(self.input)
        print(self.otp.key)

    def set_output(self, en_de):
        if en_de == 1:
            self.output = self.otp.en_de_crypt(self.input)
        else:
            self.output = self.otp.en_de_crypt(self.input, en=False)
        print(self.output)

    def get_output(self):
        print(self.output)
        return self.output

    def get_key(self):
        print(self.otp.key)
        return self.otp.key

    def get_input(self):
        print(self.input)
        return self.input
