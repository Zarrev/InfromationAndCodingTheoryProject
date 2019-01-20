from otp_encryption import OTP
import file_handler as fh

my_input = fh.get_file()
print(my_input)
otp = OTP(my_input)
print('hex-key: ', otp.key)

enc = otp.en_de_crypt(my_input)
print(enc)
fh.save_encrypted_file(enc)

tmp = fh.get_file()
print(tmp)
denc = otp.en_de_crypt(tmp, en=False)
fh.save_encrypted_file(denc)
print(denc)