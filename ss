import nn

if __name__=='__main__':      
      print "svr"

      s = nn.Socket(nn.REP)
      s.bind('tcp://127.0.0.1:1234')

      nn.serve_bindings(s, dict(
                  add = lambda a,b: str(int(a)+int(b)),
                  sub = lambda a,b: str(int(a)-int(b)),
                  ))

'''
      nn.serve_bindings->s, dict->


      nn.serve_bindings:: s, dict::
                  add = lambda a,b: str(int(a)+int(b))
                  sub = lambda a,b: str(int(a)-int(b))
'''
