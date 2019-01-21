from I.bsc_repeater.transmitter_side import Transmitter
from I.bsc_repeater.channel import Channel
from I.bsc_repeater.receiver_side import Receiver


def process(msg, repeat, prob):
    t = Transmitter(msg, repeat)
    coded = t.coded_msg
    c = Channel(coded, prob)
    sent = c.send_msg()
    r = Receiver(sent, repeat)

    return coded, c.get_err_vec(), sent, r.get_decoded()
