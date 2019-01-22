from I.bsc_repeater.receiver_side import Receiver


if __name__ == "__main__":
    r = Receiver('110011100', 3)
    print(r.received, r.repeat_num, r.decoded, sep='\n')
