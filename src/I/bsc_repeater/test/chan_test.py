from I.bsc_repeater.channel import Channel


if __name__ == "__main__":
    msg = '000111000'
    c = Channel(msg)
    print(msg, c.error_vector, c.send_msg(), sep='\n')
