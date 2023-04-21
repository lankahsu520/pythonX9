#import os, sys, errno, getopt, signal, time, io
#from time import sleep
from pythonX9 import *

#from _thread import start_new_thread
import threading

class queuex_ctx(pythonX9):

	def queuex_length(self):
		ret = 0
		if ( self.is_quit == 0 ):
			self._cond.acquire()
			ret = len(self.queue)
			self._cond.release()
		return ret

	#1: full, 0: not full
	def queuex_isfull(self):
		ret = 0
		if ( self.queuex_length() >= self.max_data ):
			#DBG_WN_LN("{} is full.".format( self.name ))
			ret = 1;
		return ret

	#1: empty, 0: not empty
	def queuex_isempty(self):
		ret = 0
		if ( self.queuex_length() == 0 ):
			ret = 1;
		return ret

	def queuex_push(self, data):
		if ( self.is_quit == 0 ):
			if ( self.queuex_isfull() == 0 ):
				self._cond.acquire()
				self.queue.append(data)
				self._cond.notify()
				self._cond.release()
			else:
				DBG_WN_LN("Skip ! (data: {})".format( data ))

	def queuex_pop(self):
		data_pop = None
		if ( self.is_quit == 0 ):
			if ( self.queuex_isempty() == 0 ):
				data_pop = self.queue.pop(0)
				if not data_pop is None:
					if not self.exec_cb is None:
						self.exec_cb(data_pop)
					#else:
					#	DBG_IF_LN(self, "(data_pop: {} / {})".format( data_pop, self.queue ) )
					if not self.free_cb is None:
						self.free_cb(data_pop)

					#sleep(500/1000)
			else:
				self.thread_sleep()

	def thread_wakeup(self):
		self._cond.acquire()
		DBG_TR_LN(self, "call notify ...")
		self._cond.notify()
		self._cond.release()

	def thread_sleep(self):
		self._cond.acquire()
		DBG_TR_LN(self, "call wait ...")
		#self._cond.wait()
		self._cond.wait(timeout=3)
		self._cond.release()

	def thread_handler(self):
		#DBG_IF_LN(self, "enter")
		self.isloop = 1
		while ( self.is_quit == 0 ):
			self.queuex_pop()
		self.isloop = 0
		DBG_WN_LN("{}".format(DBG_TXT_BYE_BYE))

	def thread_init(self):
		#start_new_thread(self.thread_handler, ())
		self._cond = threading.Condition()
		self.threading = threading.Thread(target=self.thread_handler)
		self.threading.start()
		while ( self.isloop == 0):
			sleep(1)

	def release(self):
		if ( self.is_quit == 0 ):
			self.is_quit = 1
			if ( self.threading is not None ):
				self.thread_wakeup()
				self.threading.join()
			DBG_DB_LN(self, "{}".format(DBG_TXT_DONE))

	def ctx_init(self, name, queue_size, exec_cb, free_cb):
		DBG_DB_LN(self, "{}".format(DBG_TXT_ENTER))
		self.threading = None
		self._cond = None
		self.isloop = 0

		self.queue = []

		self.name = name
		self.max_data = queue_size
		self.exec_cb = exec_cb
		self.free_cb = free_cb

	def __init__(self, name, queue_size, exec_cb, free_cb, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(queuex_ctx, self).__init__(**kwargs)

		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._kwargs = kwargs
		self.ctx_init(name, queue_size, exec_cb, free_cb)

	def parse_args(self, args):
		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._args = args

	def start(self, args={}):
		DBG_TR_LN(self, "{}".format(DBG_TXT_START))
		self.parse_args(args)
		self.thread_init()

#queuex_mgr = queuex_ctx("HelloQueueX", 10, None, None)
#queuex_mgr.release()
