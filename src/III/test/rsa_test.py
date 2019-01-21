from III import rsa_encryption as re, file_handler as fh

if __name__ == '__main__':
    rsa = re.RSA()

    input_data = fh.get_file(rsa=True)
    print('input:', input_data)

    keys = rsa.generate_keys(43, 59)
    print('keys:', keys)

    rsa.load_public_key(keys[0])
    rsa.load_private_key(keys[1])

    cipher = rsa.encrypt(input_data)
    print('encrypted:', cipher)

    plain = rsa.decrypt(cipher)
    print('decrypted:', plain)
