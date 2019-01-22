import random


class RSA:

    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.data = None

    @staticmethod
    def gcd(a, b):
        """
        This function use the Euclidean algorithm to find the greatest common divisor.
        :param a: positive integer
        :param b: positive integer
        :return: greatest common divisor
        """
        if b == 0:
            return a

        return RSA.gcd(b, a % b)

    @staticmethod
    def extended_gcd(a, b):
        """
        Implementation of the Extended Euclidean algorithm because of the modular multiplicative inverse
        :param a: positive integer
        :param b: positive integer
        :return: a mod b, b mod a, greatest common divisor
        """
        u = [1, 0, 0]
        v = [0, 1, 0]
        r = [a, b, 0]

        while r[1] != 0:
            q = r[0] // r[1]
            r[2] = r[0] % r[1]
            u[2] = u[0] - (u[1] * q)
            v[2] = v[0] - (v[1] * q)

            u[0] = u[1]
            u[1] = u[2]
            v[0] = v[1]
            v[1] = v[2]
            r[0] = r[1]
            r[1] = r[2]

        return u[0], v[0], r[0]

    @staticmethod
    def mod_inv(a, m):
        u, v, r = RSA.extended_gcd(a, m)

        if u < 0:
            u += m

        if r != 1:
            raise Exception('The remaining term must be 1. In this case the modulation invers is not exist!')

        return u

    @staticmethod
    def euler_operator(first_prime, second_prime):
        m = first_prime*second_prime
        phi_m = (first_prime-1)*(second_prime-1)
        return m, phi_m

    @staticmethod
    def choose_e(phi_m):
        """
        This function choose a appropriate 'e' value.
        :param phi_m: totient of m
        :return: the selected e what coprime with the totient
        """
        e = random.randrange(2, phi_m)

        while RSA.gcd(e, phi_m) != 1:
            e = random.randrange(2, phi_m)

        return e

    def generate_keys(self, first_prime, second_prime):
        m, totient = RSA.euler_operator(first_prime, second_prime)
        e = RSA.choose_e(totient)
        d = RSA.mod_inv(e, totient)
        public_key = (e, m)
        private_key = (first_prime, second_prime, d)
        keys = [public_key, private_key]

        return keys

    def load_public_key(self, public_key):
        self.public_key = public_key

    def load_private_key(self, private_key):
        self.private_key = private_key

    def encrypt(self, input_data):
        self.data = input_data.split(' ')
        if self.public_key is None:
            raise Exception("You cannot encrypt anything because you don't have a public key for it.")

        e = self.public_key[0]
        m = self.public_key[-1]

        ciphered = []
        for i in range(len(self.data)):
            ciphered.append(str((int(self.data[i]) ** e) % m))
            if ciphered[i] == 2:
                print(self.data[i], e, m)
                break

        return ' '.join(ciphered)

    def decrypt(self, input_data):
        self.data = input_data
        if self.private_key is None:
            raise Exception("You cannot decrypt anything because you don't have the private key for it.")

        d = self.private_key[-1]
        m = self.private_key[0] * self.private_key[1]

        ciphered = [int(x) for x in self.data.split(' ')]
        plain = []
        for i in range(len(ciphered)):
            plain.append(str((ciphered[i] ** d) % m))

        return ' '.join(plain)
