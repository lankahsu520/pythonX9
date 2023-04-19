#import os, sys, errno, getopt, signal, time, io
#from time import sleep
from pythonX9 import *

class dummy_ctx(pythonX9):
	def release(self):
		if ( self.is_quit == 0 ):
			self.is_quit = 1
			DBG_WN_LN(self, "{}".format(DBG_TXT_BYE_BYE))

	def dummy_init(self):
		DBG_DB_LN(self, "{}".format(DBG_TXT_INIT))

	def __init__(self, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(dummy_ctx, self).__init__(**kwargs)

		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._kwargs = kwargs
		self.dummy_init()

	def parse_args(self, args):
		DBG_TR_LN(self, "{}".format(DBG_TXT_ENTER))
		self._args = args

	def start(self, args={}):
		DBG_TR_LN(self, "{}".format(DBG_TXT_START))
		self.parse_args(args)

#dummy_mgr = dummy_ctx()
#dummy_mgr.release()
