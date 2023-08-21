#Simple example python program that send a signal between two threads

import gobject
import threading
import time

class knight(gobject.GObject):
    __gsignals__ = { 'chicken': (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE,
                                   (str,)) }
    def __init__(self) :
        #Call super()
        gobject.GObject.__init__(self)
        #Do your initialization here
        #This is only an example
        a = None
        
class tv_speaker :
    def __init__(self,emiter) :
        self.emiter = emiter
        self.emiter.connect("chicken",self.do)
        
    def do(self,param1,param2) :
        print "receiving the chicken on the head : my brain hurt"
        time.sleep(2)
        print "And now for something completely %s" %param2
        
class chapman :
    def __init__(self,emiter) :
        self.emiter = emiter
        
    def connect(self,signal,func) :
        self.emiter.connect(signal,func)

k = knight()
c = chapman(k)
tv = tv_speaker(c)
k.emit("chicken","different")
k.emit("chicken","random")
