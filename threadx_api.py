#import os, sys, errno, getopt, signal, time, io
#from time import sleep
from pythonX9 import *

#from _thread import start_new_thread
import threading

class threadx_ctx(object):

	def threadx_set_loop(self, isloop):
		self.isloop = isloop

	def threadx_isloop(self):
		return self.isloop

	def threadx_lock(self):
		self._cond.acquire()

	def threadx_unlock(self):
		self._cond.release()

	def threadx_notify(self):
		self._cond.notify()

	def threadx_join(self):
		self.threading.join()

	def threadx_wait(self, itimeout=3):
		self._cond.wait(timeout=itimeout)

	def threadx_wakeup(self):
		self.threadx_lock()
		DBG_TR_LN(self, "call notify ...")
		self.threadx_notify()
		self.threadx_unlock()

	def threadx_sleep(self, itimeout=3):
		self.threadx_lock()
		DBG_TR_LN(self, "call wait ... (itimeout: {})".format(itimeout))
		#self._cond.wait()
		self.threadx_wait(itimeout)
		self.threadx_unlock()

	def threadx_init(self):
		#start_new_thread(self.threadx_handler, ())
		self._cond = threading.Condition()
		self.threading = threading.Thread(target=self.threadx_handler)
		self.threading.start()
		while ( self.threadx_isloop()== 0):
			sleep(1)

	def threadx_handler(self):
		#DBG_IF_LN(self, "enter")
		self.threadx_set_loop(1)
		DBG_WN_LN(self, "Please override this function !!!")
		self.threadx_set_loop(0)
		DBG_WN_LN("{}".format(DBG_TXT_BYE_BYE))

	def __init__(self, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(threadx_ctx, self).__init__(**kwargs)

		self.isloop = 0
		self.threading = None
		self._cond = None

