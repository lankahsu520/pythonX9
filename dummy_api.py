#import os, sys, errno, getopt, signal, time, io
#from time import sleep
from pythonX9 import *

class dummy_ctx(pythonX9):
	def release(self):
		DBG_WN_LN(self, "enter")
		self.is_quit = 1

	def dummy_init(self):
		DBG_DB_LN(self, "enter")

	def __init__(self, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(dummy_ctx, self).__init__(**kwargs)

		self._kwargs = kwargs
		self.dummy_init()

	def parse_args(self, args):
		self._args = args

	def start(self, args={}):
		self.parse_args(args)

#dummy_mgr = dummy_ctx()
#dummy_mgr.release()
