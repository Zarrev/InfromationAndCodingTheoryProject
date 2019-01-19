from otp_encryption import gen_key, en_de_crypt

msg = "Nézzük, hogy működik-e!"
key = gen_key(len(msg))
ctext = en_de_crypt(msg, key)
print(ctext)
print(en_de_crypt(ctext, key, False))