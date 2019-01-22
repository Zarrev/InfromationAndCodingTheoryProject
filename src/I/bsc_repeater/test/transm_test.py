from I.bsc_repeater.transmitter_side import Transmitter


if __name__ == "__main__":
    t = Transmitter('010', 3)
    print(t.coded_msg)
