from abc import abstractmethod, ABCMeta


class Model(metaclass=ABCMeta):
    """
    This class is the parent of the other model classes. It implements the common functions and it contains some
    abstract method for the later use.
    """

    def __init__(self):
        self.input = None
        self.output = None

    def set_input(self, _input):
        self.input = _input
        print(self.input)

    def get_output(self):
        print(self.output)
        return self.output

    def get_input(self):
        print(self.input)
        return self.input

    @abstractmethod
    def set_output(self, en_de):
        """
        Set the appropriate class variable - self.output
        :param en_de: This parameter gives the function's mode. The options: encryption, decryption.
        """

    @abstractmethod
    def set_key(self, en_de):
        """
        Set a key value of a child's class variable - For example: OTP, RSA
        :param en_de: This parameter gives the function's mode. The options: encryption, decryption.
        """