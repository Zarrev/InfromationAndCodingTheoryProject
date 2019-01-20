import random

class RSA:

    def __init__(self):
        pass

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
        :param a:
        :param b:
        :return:
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

    def euler_operator(self, first_prime, second_prime):
        m = first_prime*second_prime
        phi_m = (first_prime-1)*(second_prime-1)
        return m, phi_m

    def choose_e(self, phi_m):
        """
        This function choose a appropriate 'e' value. The randrange let the 1 possible value as well because Győri
        Vajda's book says that. (However I found it strange.)
        :param phi_m: totient of m
        :return: the selected e what coprime with the totient
        """
        e = random.randrange(1, phi_m)

        while RSA.gcd(e, phi_m) != 1:
            e = random.randrange(1, phi_m-1)

        return e


if __name__ == '__main__':
    RSA = RSA()
    e_o = RSA.euler_operator(3, 5)
    e = RSA.choose_e(e_o[-1])
    d = RSA.extended_gcd(7, e_o[-1])
    print(e_o, e, d)