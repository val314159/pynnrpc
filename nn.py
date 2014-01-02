from nanomsg import *
#from cPickle import loads, dumps
from msgpack import loads, dumps
#from json import loads, dumps
#from coder import loads, dumps

def send_recv(s,data):
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
        print "-"*80
        print repr(d)
        print "-"*80
        fn = binder.get(d[0], None)
        print "FN", fn
        xx = fn(*d[1],**d[2])
        return xx
    return fn2

def bind_remote_dict(s,binder):
    return recv_send(s,remote_binding_dict(binder))

def serve_bindings(s,binder):
    while 1: bind_remote_dict(s,binder)
