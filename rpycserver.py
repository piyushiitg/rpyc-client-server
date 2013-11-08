from rpyc.utils import server
import rpyc
import time
class DoStuffService(rpyc.Service):
   def on_connect(self):
       print "Do some things when a connection is made"
   def on_disconnect(self):
       print "Do some things AFTER a connection is dropped"
   def exposed_func1(self, *args, **kws):
       return "Hello World"
   def exposed_func2(self, *args, **kws):
       print "Like func1, but do something different"

if __name__ == '__main__':
   protocol_config = dict(instantiate_custom_exceptions=True, import_custom_exceptions=True)
   server.ThreadedServer(DoStuffService,hostname='localhost', port=8888,auto_register=False, protocol_config=protocol_config, backlog=500).start()
