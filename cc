import nn

if __name__=='__main__':      
    print "clt"

    s = nn.Socket(nn.REQ)
    s.connect('tcp://127.0.0.1:1234')

    b = nn.RemoteBinder(s)

    r = b.sub('100','21')
    print "xxxxRRRRR w", repr(r)

    r = b.add('100','21')
    print "xxxxRRRRR x", repr(r)
