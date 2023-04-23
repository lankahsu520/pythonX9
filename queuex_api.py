#import os, sys, errno, getopt, signal, time, io
#from time import sleep
from pythonX9 import *
from threadx_api import *

class queuex_ctx(pythonX9, threadx_ctx):

	def queuex_length(self):
		ret = 0
		self.threadx_lock()
		ret = len(self.items)
		self.threadx_unlock()
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

	#1: sleep, 0: normal
	def queuex_ishold(self):
		return self._is_hold

	def queuex_gosleep(self):
		if ( self.threadx_inloop() == 1 ):
			self.threadx_lock()
			self._is_hold = 1
			self.threadx_unlock()

	def queuex_wakeup(self):
		if ( self.threadx_inloop() == 1 ):
			self.threadx_lock()
			self._is_hold = 0
			self.threadx_notify()
			self.threadx_unlock()

	def queuex_push(self, data):
		if ( self.is_quit == 0 ) and ( self.threadx_inloop() == 1):
			if ( self.queuex_isfull() == 0 ):
				self.threadx_lock()
				self.items.append(data)
				if ( (self._is_sort == 1) and (self._dict_key != "") ):
					self.items.sort(key=lambda x: (x[self._dict_key]))
				if ( self.queuex_ishold() == 0 ):
					self.threadx_notify()
				self.threadx_unlock()
			else:
				DBG_WN_LN("Skip ! (data: {})".format( data ))

	def queuex_pop(self):
		data_pop = None
		if ( self.is_quit == 0 ):
			if ( self.queuex_isempty() == 0 ) and ( self.queuex_ishold() == 0 ):
				self.threadx_lock()
				idx = 0
				if ( self._is_stack == 1 ):
					idx = -1
				data_pop = self.items.pop(idx)
				self.threadx_unlock()

				if not data_pop is None:
					if not self.exec_cb is None:
						self.exec_cb(data_pop)
					#else:
					#	DBG_IF_LN(self, "(data_pop: {} / {})".format( data_pop, self.items ) )
					if not self.free_cb is None:
						self.free_cb(data_pop)
					#sleep(3/1000)
			else:
				self.threadx_sleep(3)

	def threadx_handler(self):
		#DBG_IF_LN(self, "enter")
		self.threadx_set_inloop(1)
		while ( self.is_quit == 0 ):
			self.queuex_pop()
		self.threadx_set_inloop(0)
		DBG_WN_LN("{}".format(DBG_TXT_BYE_BYE))

	def release(self):
		if ( self.is_quit == 0 ):
			self.is_quit = 1
			if ( self.threadx_inloop() == 1 ):
				self.threadx_wakeup()
				self.threadx_join()
			DBG_DB_LN(self, "{}".format(DBG_TXT_DONE))

	def ctx_init(self, name, queue_size, exec_cb, free_cb, is_hold=0, is_stack=0, is_sort=0, dict_key=""):
		DBG_DB_LN(self, "{}".format(DBG_TXT_ENTER))

		self.items = []

		self.name = name
		self.max_data = queue_size
		self.exec_cb = exec_cb
		self.free_cb = free_cb
		self._is_hold = is_hold
		self._is_stack = is_stack
		self._is_sort = is_sort
		self._dict_key = dict_key

	def __init__(self, name, queue_size, exec_cb, free_cb, is_hold=0, is_stack=0, is_sort=0, dict_key="", **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(queuex_ctx, self).__init__(**kwargs)

		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._kwargs = kwargs
		self.ctx_init(name, queue_size, exec_cb, free_cb, is_hold, is_stack, is_sort, dict_key)

	def parse_args(self, args):
		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._args = args

	def start(self, args={}):
		DBG_TR_LN(self, "{}".format(DBG_TXT_START))
		self.parse_args(args)
		self.threadx_init()

#queuex_mgr = queuex_ctx("HelloQueueX", 10, None, None)
#queuex_mgr.release()
