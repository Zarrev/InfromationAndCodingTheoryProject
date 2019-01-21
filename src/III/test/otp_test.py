from III.otp_encryption import OTP
from III import file_handler as fh

if __name__ == '__main__':
    my_input = fh.get_file()
    # print(my_input)
    otp = OTP()
    otp.gen_key(my_input)
    # print('hex-key: ', otp.key)

    enc = otp.en_de_crypt(my_input)
    # print(enc)
    # fh.save_key(otp.key, 'key_of_otp')
    fh.save_encrypted_file(enc)
    # otp.key = ''

    tmp = fh.get_file()
    # otp.key = fh.load_key()
    # print(tmp)
    denc = otp.en_de_crypt(tmp, en=False)
    fh.save_encrypted_file(denc)
    # print(denc)
