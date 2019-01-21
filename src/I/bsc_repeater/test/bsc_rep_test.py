from I.bsc_repeater.transmitter_side import Transmitter
from I.bsc_repeater.channel import Channel
from I.bsc_repeater.receiver_side import Receiver

msg = '010'
rep = 3
t = Transmitter('010', rep)
coded = t.coded_msg
print(coded)
c = Channel(coded)
sent = c.send_msg()
print(t.coded_msg, c.error_vector, sent, sep='\n')
r = Receiver(sent, rep)
print(r.received, r.repeat_num, r.decoded, sep='\n')
