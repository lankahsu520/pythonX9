#import os, sys, errno, getopt, signal, time, io
#from time import sleep
from pythonX9 import *
from threadx_api import *

class statex_ctx(pythonX9, threadx_ctx):

	def statex_length(self):
		ret = 0
		self.threadx_lock()
		ret = len(self.items)
		self.threadx_unlock()
		return ret

	#1: full, 0: not full
	def statex_isfull(self):
		ret = 0
		if ( self.statex_length() >= self.max_data ):
			#DBG_WN_LN("{} is full.".format( self.name ))
			ret = 1;
		return ret

	#1: empty, 0: not empty
	def statex_isempty(self):
		ret = 0
		if ( self.statex_length() == 0 ):
			ret = 1;
		return ret

	#1: sleep, 0: normal
	def statex_ishold(self):
		return self._is_hold

	def statex_gosleep(self):
		if ( self.threadx_inloop() == 1 ):
			self.threadx_lock()
			self._is_hold = 1
			self.threadx_unlock()

	def statex_wakeup(self):
		if ( self.threadx_inloop() == 1 ):
			self.threadx_lock()
			self._is_hold = 0
			self.threadx_notify()
			self.threadx_unlock()

	#def statex_push(self, name="", priority=999, exec_cb=None, free_cb=None):
	def statex_push(self, data):
		if ( self.is_quit == 0 ) and ( self.threadx_inloop() == 1):
			if ( self.statex_isfull() == 0 ):
				self.threadx_lock()
				#item={ "name": name, "priority": priority, "exec_cb": exec_cb, "free_cb": free_cb }
				item=data
				DBG_DB_LN("(name: {})".format( item["name"] ))
				if (not item["init_cb"] is None):
					item["init_cb"](item)
				self.items.append(item)
				self.items.sort(key=lambda x: (x["priority"]))
				if ( self.statex_ishold() == 0 ):
					self.threadx_notify()
				self.threadx_unlock()

	def statex_pop(self):
		data_pop = None
		if ( self.is_quit == 0 ):
			if ( self.statex_isempty() == 0 ):
				change = 0

				self.threadx_lock()
				idx = 0
				data_pop = self.items.pop(idx)
				self.threadx_unlock()

				DBG_DB_LN("(name: {})".format( data_pop["name"] ))
				item = data_pop
				if ( self._last_data == item ):
					self._last_data = None
					change = 1

				if ( change == 1 ):
					self.statex_switch()
					if (not data_pop["leave_cb"] is None):
						data_pop["leave_cb"](data_pop)

	def statex_remove(self, data):
		data_pop = None
		if ( self.is_quit == 0 ):
			if ( self.statex_isempty() == 0 ):
				change = 0

				DBG_DB_LN("(name: {})".format( data["name"] ))
				self.threadx_lock()
				for item in self.items:
					if (item["name"] == data["name"]):

						if ( self._last_data["name"] == item["name"] ):
							self._last_data = None
							change = 1

						data_pop = item
						self.items.remove(item)
				self.threadx_unlock()

				if ( change == 1 ):
					self.statex_switch()
					if (not data_pop["leave_cb"] is None):
						data_pop["leave_cb"](data_pop)

	def statex_switch(self):
		data_pop = None
		if ( self.is_quit == 0 ):
			if ( self.statex_isempty() == 0 ):
				self.threadx_lock()
				idx = 0
				data_pop = self.items[idx]
				self.threadx_unlock()

				change = 0
				if self._last_data is None:
					if not data_pop["exec_cb"] is None:
						data_pop["exec_cb"](data_pop)
					self._last_data = data_pop

				elif (self._last_data != data_pop):
					if not data_pop["exec_cb"] is None:
						data_pop["exec_cb"](data_pop)
					if (not self._last_data["leave_cb"] is None):
							self._last_data["leave_cb"](self._last_data)
					self._last_data= data_pop

			else:
				self.threadx_sleep(0)

	def statex_exec_cb(self):
		data_pop = None
		if ( self.is_quit == 0 ):
			if ( self.statex_isempty() == 0 ) and ( self.statex_ishold() == 0 ):
				self.statex_switch()
				self.threadx_sleep(0)
			else:
				self.threadx_sleep(3)

	def threadx_handler(self):
		#DBG_IF_LN(self, "enter")
		self.threadx_set_inloop(1)
		while ( self.is_quit == 0 ):
			self.statex_exec_cb()
		self.threadx_set_inloop(0)
		DBG_WN_LN("{}".format(DBG_TXT_BYE_BYE))

	def release(self):
		if ( self.is_quit == 0 ):
			self.is_quit = 1
			if ( self.threadx_inloop() == 1 ):
				self.threadx_wakeup()
				self.threadx_join()
			DBG_DB_LN(self, "{}".format(DBG_TXT_DONE))

	def ctx_init(self, name, state_size, is_hold=0):
		DBG_DB_LN(self, "{}".format(DBG_TXT_ENTER))

		self.items = []

		self.name = name
		self.max_data = state_size
		self._is_hold = is_hold
		self._last_data = None

	def __init__(self, name, state_size=20, is_hold=0, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(statex_ctx, self).__init__(**kwargs)

		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._kwargs = kwargs
		self.ctx_init(name, state_size, is_hold)

	def parse_args(self, args):
		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._args = args

	def start(self, args={}):
		DBG_TR_LN(self, "{}".format(DBG_TXT_START))
		self.parse_args(args)
		self.threadx_init()

#statex_mgr = statex_ctx("HelloStateX", 30, 0)
#statex_mgr.release()
