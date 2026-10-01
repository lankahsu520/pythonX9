# -*- coding: utf-8 -*-
"""
 ***************************************************************************
 * Copyright (C) 2023, Lanka Hsu, <lankahsu@gmail.com>, et al.
 *
 * This software is licensed as described in the file COPYING, which
 * you should have received as part of this distribution.
 *
 * You may opt to use, copy, modify, merge, publish, distribute and/or sell
 * copies of the Software, and permit persons to whom the Software is
 * furnished to do so, under the terms of the COPYING file.
 *
 * This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY
 * KIND, either express or implied.
 *
 ***************************************************************************
"""

#import os, sys, errno, getopt, signal, time, io
#from time import sleep
from pythonX9 import *

#from _thread import start_new_thread
import threading

class threadx_ctx(object):

	def threadx_set_inloop(self, inloop):
		if (self._inloop is not None):
			self._inloop = inloop

	def threadx_inloop(self):
		if (self._inloop is not None):
			return self._inloop

	def threadx_lock(self):
		if (self._cond is not None):
			self._cond.acquire()

	def threadx_unlock(self):
		if (self._cond is not None):
			self._cond.release()

	def threadx_notify(self):
		if (self._cond is not None):
			self._cond.notify()

	def threadx_join(self):
		if (self._threading is not None):
			self._threading.join()

	def threadx_wait(self, timeout=1):
		if (self._cond is not None):
			if ( timeout >0 ):
				self._cond.wait(timeout=timeout)
			else:
				self._cond.wait()

	def threadx_wakeup(self):
		self.threadx_lock()
		DBG_TR_LN("call notify ...")
		self.threadx_notify()
		self.threadx_unlock()

	def threadx_sleep(self, timeout=1):
		self.threadx_lock()
		DBG_TR_LN("call wait ... (timeout: {})".format(timeout))
		#self._cond.wait()
		self.threadx_wait(timeout)
		self.threadx_unlock()

	def threadx_init(self):
		#start_new_thread(self.threadx_handler, ())
		self._cond = threading.Condition()
		self._threading = threading.Thread(target=self.threadx_handler)
		self._threading.start()
		while ( self.threadx_inloop()== 0):
			sleep(1)

	def threadx_handler(self):
		#DBG_IF_LN("{}".format(DBG_TXT_ENTER))
		self.threadx_set_inloop(1)
		DBG_WN_LN("Please override this function !!!")
		self.threadx_set_inloop(0)
		DBG_WN_LN("{}".format(DBG_TXT_BYE_BYE))

	def __init__(self, **kwargs):
		if ( isPYTHON(PYTHON_V3) ):
			super().__init__(**kwargs)
		else:
			super(threadx_ctx, self).__init__(**kwargs)

		self._inloop = 0
		self._threading = None
		self._cond = None


