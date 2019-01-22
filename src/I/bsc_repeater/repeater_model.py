from I.bsc_repeater.transmitter_side import Transmitter
from I.bsc_repeater.channel import Channel
from I.bsc_repeater.receiver_side import Receiver

p_b = []
correct = []

def process(msg, repeat, prob):
    t = Transmitter(msg, repeat)
    coded = t.coded_msg
    c = Channel(coded, prob)
    sent = c.send_msg()
    r = Receiver(sent, repeat)

    p_b.append(prob)
    correct.append(1 if msg == r.get_decoded() else 0)

    return coded, c.get_err_vec(), sent, r.get_decoded()