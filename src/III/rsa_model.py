from III import rsa_encryption as re, origin_model as om


class RSA_M(om.Model):

    def __init__(self):
        super().__init__()
        self.rsa = re.RSA()

    def set_input(self, _input):
        self.input = _input
        print(self.input)

    def set_key(self, key, en_de=1):
        if en_de == 1:
            self.rsa.load_public_key(key)
            print('public:', self.rsa.public_key)
        else:
            self.rsa.load_private_key(key)
            print('private', self.rsa.private_key)

    def set_output(self, en_de):
        if en_de == 1:
            self.output = self.rsa.encrypt(self.input)
        else:
            self.output = self.rsa.decrypt(self.input)
        print(self.output)

    def get_output(self):
        print(self.output)
        return self.output

    def get_input(self):
        print(self.input)
        return self.input

    def get_key(self, p, q):
        return self.rsa.generate_keys(p, q)
