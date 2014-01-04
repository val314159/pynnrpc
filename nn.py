from nanomsg import *
#from cPickle import loads, dumps
from msgpack import loads, dumps
#from json import loads, dumps
#from coder import loads, dumps

def send_recv(s,data):
    """
    convenience function to perform a send and a recv in one step.
    """
    e = dumps(data)
    s.send(e)
    r = s.recv()
    d = loads(r)
    return d

def recv_send(s,fn):
    r = s.recv()
    d = loads(r)
    x = fn(s,d)
    e = dumps(x)
    s.send(e)
    return

class RemoteBinder:
    def __init__(_, s): _.s = s
    def __getattr__(_, attr):
        return lambda *a, **kw: send_recv(_.s,[attr,a,kw])
    pass # class RemoteBinder

def remote_binding_dict(binder):
    def fn2(s,d):
        #print "-"*80
        #print repr(d)
        #print "-"*80
        fn = binder.get(d[0], None)
        #print "FN", fn
        xx = fn(*d[1],**d[2])
        return xx
    return fn2

def bind_remote_dict(s,binder):
    return recv_send(s,remote_binding_dict(binder))

def serve_bindings(s,binder):
    while 1: bind_remote_dict(s,binder)

_types = dict(PUB=PUB,SUB=SUB,REQ=REQ,REP=REP)

def make_socket(url):
    print "URL ", repr(url)
    print url[0]
    pfx = url[0]
    url2 = url[1:]
    transport, other = url2.split('::',1)
    print "ARR1", transport, other
    typ = _types[transport]
    print "TYP ", typ
    print "URL", other

    print "QQQQ", other
    arr = other.split('/',3)
    print "ARR2", arr
    subarr = arr[3:4]    
    print "ARR3", subarr

    newurl = '/'.join(arr[:3])
    print "NU", newurl

    s = Socket(typ)
    if pfx == '+':
        s.connect(newurl)
    elif pfx == '-':
        s.bind(newurl)

    if typ == SUB  and  subarr:
        print "DO IT"
        subscribe(s, subarr[0])
        pass

    return s

def subscribe(s, pat=''):
    s.set_string_option(SUB, SUB_SUBSCRIBE, pat)
    pass

Socket.raw_recv = Socket.recv
Socket.send_recv = Socket.send

def recv2(s):
    return loads(s.recv())

def send2(s,d):
    return dumps(s.send(d))

Socket.recv2 = recv2
Socket.send2 = send2
